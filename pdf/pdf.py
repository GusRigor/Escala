from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from pdf.cabecalho import criar_cabecalho

# Cria o PDF
def criar_pdf(escala, arquivo="escala_enfermagem.pdf"):
    c = canvas.Canvas(arquivo, pagesize=landscape(A4))
    largura, altura = landscape(A4)

    criar_cabecalho(c, largura, altura, "Junho de 2025", "Maternidade Bárbara Heliodora")

    
    # c.setFont("Helvetica-Bold", 12)
    # c.drawString(2 * cm, altura - 3 * cm, "Data")
    # c.drawString(5 * cm, altura - 3 * cm, "Manhã")
    # c.drawString(10 * cm, altura - 3 * cm, "Tarde")
    # c.drawString(15 * cm, altura - 3 * cm, "Noite")

    # c.setFont("Helvetica", 11)
    # y = altura - 3.7 * cm

    # for dia in escala:
    #     c.drawString(2 * cm, y, dia["data"])
    #     c.drawString(5 * cm, y, dia["Manhã"])
    #     c.drawString(10 * cm, y, dia["Tarde"])
    #     c.drawString(15 * cm, y, dia["Noite"])
    #     y -= 0.6 * cm

    #     if y < 2 * cm:
    #         c.showPage()
    #         y = altura - 3 * cm
    #         c.setFont("Helvetica", 11)

    c.save()
    print(f"✅ PDF gerado com sucesso: {arquivo}")