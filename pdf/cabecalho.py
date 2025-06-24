from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def criar_cabecalho(c, largura, altura, mes, institicao):
    # Define a fonte e tamanho do cabeçalho
    c.setFont("Helvetica-Bold", 16)
    
    # Desenha o título do cabeçalho
    titulo = "RESIDÊNCIA EM ENFERMAGEM OBSTÉTRICA"
    c.drawString(2 * cm, altura - 2 * cm, titulo)
    
    # Desenha o subtítulo
    subtitulo = "Escala de Trabalho e Atividades de Estudo"
    c.drawString(2 * cm, altura - 2.5 * cm, subtitulo)

    # Desenha o mês
    c.setFont("Helvetica", 12)
    c.drawString(2 * cm, altura - 3 * cm, "Mês:")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(3 * cm, altura - 3 * cm, mes)

    # Desenha o instituição
    c.setFont("Helvetica", 12)
    c.drawString(2 * cm, altura - 3.5 * cm, "Instituição:")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(4.1 * cm, altura - 3.5 * cm, institicao)
    