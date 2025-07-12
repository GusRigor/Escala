import io
import base64
from PIL import Image, UnidentifiedImageError
import pytesseract
import numpy as np
import cv2
import pandas as pd

def _processa_foto_(imagem=None, imagem_base64=None) -> str:
    """
    Processa uma imagem enviada (arquivo ou base64), melhora com OpenCV,
    executa OCR usando pytesseract no modo TSV e retorna texto organizado como tabela.

    Args:
        imagem: Objeto de arquivo enviado (com .chunks()).
        imagem_base64: String base64 (dataURL) da imagem recortada.

    Returns:
        Texto extraído da imagem, em formato mais próximo de tabela.
    """
    try:
        if imagem_base64:
            if "," in imagem_base64:
                imagem_base64 = imagem_base64.split(",")[1]
            image_bytes = io.BytesIO(base64.b64decode(imagem_base64))
        elif imagem:
            image_bytes = io.BytesIO()
            for chunk in imagem.chunks():
                image_bytes.write(chunk)
            image_bytes.seek(0)
        else:
            return "Nenhuma imagem fornecida."

        # Carrega imagem em OpenCV
        file_bytes = np.asarray(bytearray(image_bytes.read()), dtype=np.uint8)
        img_cv = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img_cv is None:
            return "Erro: Não foi possível decodificar a imagem."

        # Pré-processamento
        gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        binary = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 10
        )
        kernel = np.ones((2, 2), np.uint8)
        cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
        processed = cv2.bitwise_not(cleaned)

        img_pil = Image.fromarray(processed)

        # Usa modo TSV para obter posições
        tsv_data = pytesseract.image_to_data(
            img_pil, lang="por", config="--psm 6", output_type=pytesseract.Output.DATAFRAME
        )

        if tsv_data.empty or 'text' not in tsv_data:
            return "Nenhum texto detectado."

        # Remove linhas sem texto
        tsv_data = tsv_data[tsv_data['text'].notnull() & (tsv_data['text'].str.strip() != '')]

        if tsv_data.empty:
            return "Nenhum texto detectado."

        # Agrupa por linha aproximada (y)
        tsv_data['line_id'] = (tsv_data['top'] / 20).round().astype(int)

        linhas = []
        for _, grupo in tsv_data.groupby('line_id'):
            # Ordena as palavras por x
            grupo = grupo.sort_values('left')
            linha = []
            last_right = 0
            for _, word in grupo.iterrows():
                # insere espaços conforme necessário
                spaces = max(0, (word['left'] - last_right) // 30)
                linha.append(' ' * spaces + word['text'])
                last_right = word['left'] + word['width']
            linhas.append(' '.join(linha))

        return '\n'.join(linhas)

    except UnidentifiedImageError:
        return "Erro: Arquivo enviado não é uma imagem válida."
    except Exception as e:
        return f"Erro ao processar a imagem: {e}"