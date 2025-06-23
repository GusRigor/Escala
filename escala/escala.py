from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import datetime, timedelta

# Dados da escala
nomes = ["Enfermeira Ana", "Enfermeira Bruno", "Enfermeira Carla"]
turnos = ["Manhã", "Tarde", "Noite"]
inicio_mes = datetime(2025, 7, 1)
dias_do_mes = 31

# Gera a escala automaticamente alternando os nomes
def gerar_escala(nomes: list = nomes, turnos: list = turnos, inicio_mes: datetime = inicio_mes, dias_do_mes: int = dias_do_mes):
    escala = []
    for i in range(dias_do_mes):
        data = inicio_mes + timedelta(days=i)
        linha = {
            "data": data.strftime("%d/%m/%Y"),
            "Manhã": nomes[(i * 3 + 0) % len(nomes)],
            "Tarde": nomes[(i * 3 + 1) % len(nomes)],
            "Noite": nomes[(i * 3 + 2) % len(nomes)],
        }
        escala.append(linha)
    return escala

# Cria o PDF
def criar_pdf(escala, arquivo="escala_enfermagem.pdf"):
    c = canvas.Canvas(arquivo, pagesize=A4)
    largura, altura = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(2 * cm, altura - 2 * cm, "Escala de Enfermagem - Julho 2025")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, altura - 3 * cm, "Data")
    c.drawString(5 * cm, altura - 3 * cm, "Manhã")
    c.drawString(10 * cm, altura - 3 * cm, "Tarde")
    c.drawString(15 * cm, altura - 3 * cm, "Noite")

    c.setFont("Helvetica", 11)
    y = altura - 3.7 * cm

    for dia in escala:
        c.drawString(2 * cm, y, dia["data"])
        c.drawString(5 * cm, y, dia["Manhã"])
        c.drawString(10 * cm, y, dia["Tarde"])
        c.drawString(15 * cm, y, dia["Noite"])
        y -= 0.6 * cm

        if y < 2 * cm:
            c.showPage()
            y = altura - 3 * cm
            c.setFont("Helvetica", 11)

    c.save()
    print(f"✅ PDF gerado com sucesso: {arquivo}")