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
    
    meses_numero = {
        "1": "Janeiro",
        "2": "Fevereiro",
        "3": "Março",
        "4": "Abril",
        "5": "Maio",
        "6": "Junho",
        "7": "Julho",
        "8": "Agosto",
        "9": "Setembro",
        "10": "Outubro",
        "11": "Novembro",
        "12": "Dezembro"
    }

    if str(nome_ingles).isdigit():
        return meses_numero.get(str(int(nome_ingles)), "-")
    return meses.get(nome_ingles, "-")

def eh_fim_de_semana(dia: date) -> bool:
    return dia.weekday() >= 5

def to_date(ano: int, mes: int) -> date:
    return date(ano, mes, 1)