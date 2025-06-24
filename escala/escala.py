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