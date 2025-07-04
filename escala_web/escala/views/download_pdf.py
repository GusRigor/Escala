from django.http import FileResponse, Http404
import os
from datetime import datetime

def download_pdf(request):
    caminho_pdf = os.path.join('source', 'latex', 'main.pdf')
    if not os.path.exists(caminho_pdf):
        raise Http404("Arquivo não encontrado")

    filename = f'escala-{datetime.now()}.pdf'
    return FileResponse(open(caminho_pdf, 'rb'), as_attachment=True, filename=filename)
