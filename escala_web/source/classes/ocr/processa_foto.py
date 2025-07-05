import tempfile
from PIL import Image
import pytesseract

def _processa_foto_(imagem):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        for chunk in imagem.chunks():
            tmp.write(chunk)
        tmp_path = tmp.name

    img = Image.open(tmp_path)
    texto = pytesseract.image_to_string(img, lang="por")
    return texto


