import io
import base64
from PIL import Image, UnidentifiedImageError
import pytesseract

def _processa_foto_(imagem=None, imagem_base64=None) -> str:
    """
    Processa uma imagem enviada (arquivo ou base64),
    executa OCR usando pytesseract e retorna o texto extraído.

    Args:
        imagem: Objeto de arquivo enviado (com .chunks()).
        imagem_base64: String base64 (dataURL) da imagem recortada.

    Returns:
        Texto extraído da imagem, ou mensagem de erro.
    """
    try:
        if imagem_base64:
            # Remove o cabeçalho "data:image/png;base64,"
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

        img = Image.open(image_bytes)
        texto = pytesseract.image_to_string(img, lang="por")
        return texto.strip()
    except UnidentifiedImageError:
        return "Erro: Arquivo enviado não é uma imagem válida."
    except Exception as e:
        return f"Erro ao processar a imagem: {e}"
