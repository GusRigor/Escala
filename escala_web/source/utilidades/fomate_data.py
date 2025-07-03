from datetime import date

def dia_semana_portugues(abreviacao_ingles):
    dias_semana = {
        "Mon": "S",
        "Tue": "T",
        "Wed": "Q",
        "Thu": "Q",
        "Fri": "S",
        "Sat": "S",
        "Sun": "D"
    }
    return dias_semana.get(abreviacao_ingles, "-")

def mes_portugues(nome_ingles):
    meses = {
        "January": "Janeiro",
        "February": "Fevereiro",
        "March": "Março",
        "April": "Abril",
        "May": "Maio",
        "June": "Junho",
        "July": "Julho",
        "August": "Agosto",
        "September": "Setembro",
        "October": "Outubro",
        "November": "Novembro",
        "December": "Dezembro"
    }
    return meses.get(nome_ingles, "-")

def eh_fim_de_semana(dia: date) -> bool:
    return dia.weekday() >= 5