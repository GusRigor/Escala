import io
import base64
from PIL import Image
import pytesseract
import numpy as np
import cv2
from source.enums.valorEscala import ValorEscala

VALORES_VALIDOS = {e.value for e in ValorEscala}

def _processa_foto_(
    imagem=None,
    imagem_base64=None,
    n_colunas=31,
    default_linha1=ValorEscala.TARDE.value,
    default_linha2=ValorEscala.PLANTAO_NOTURNO.value
):
    """
    Processa a imagem de tabela, corta em duas linhas, divide em colunas iguais e valida célula por célula.
    """
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

    file_bytes = np.asarray(bytearray(image_bytes.read()), dtype=np.uint8)
    img_cv = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img_cv is None:
        return "Erro: Não foi possível decodificar a imagem."

    altura, largura = img_cv.shape[:2]
    meio_y = altura // 2

    cell_width = largura / n_colunas

    linha1 = []
    linha2 = []

    for i in range(n_colunas):
        x_start = int(i * cell_width)
        x_end = int((i + 1) * cell_width)

        # Primeira linha
        cell1 = img_cv[0:meio_y, x_start:x_end]
        val1 = ocr_celula(cell1)
        if val1 in VALORES_VALIDOS:
            linha1.append(val1)
        elif val1 != '':
            linha1.append(default_linha1)
        else:
            linha1.append('')

        # Segunda linha
        cell2 = img_cv[meio_y:altura, x_start:x_end]
        val2 = ocr_celula(cell2)
        if val2 in VALORES_VALIDOS:
            linha2.append(val2)
        elif val2 != '':
            linha2.append(default_linha2)
        else:
            linha2.append('')

    return linha1, linha2

def ocr_celula(celula_cv, min_conf=60):
    """
    Executa OCR em uma célula e retorna texto limpo se confiança for aceitável.
    """
    img_pil = Image.fromarray(celula_cv)
    data = pytesseract.image_to_data(
        img_pil,
        lang='por',
        config='--psm 10',
        output_type=pytesseract.Output.DICT
    )
    n = len(data['text'])
    for i in range(n):
        texto = data['text'][i].strip().upper()
        try:
            conf = float(data['conf'][i])
        except ValueError:
            conf = -1
        if texto != '' and conf >= min_conf:
            return texto
    return ''