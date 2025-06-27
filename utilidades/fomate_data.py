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