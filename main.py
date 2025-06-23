from datetime import datetime, timedelta
from escala.escala import gerar_escala, criar_pdf

def main():
    # Dados de entrada
    nomes = ["Enfermeira A", "Enfermeira B", "Enfermeira C"]
    turnos = ["Manhã", "Tarde", "Noite"]
    inicio_mes = datetime(2025, 7, 1)
    dias_do_mes = 31
    # Chama a função principal para gerar a escala e o PDF
    escala = gerar_escala(nomes, turnos, inicio_mes, dias_do_mes)
    criar_pdf(escala)

    # Executa tudo
if __name__ == "__main__":
    main()
