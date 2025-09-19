def recomendar_sala(participantes, tipo_reuniao):
    if participantes < 0:
        return "Número de participantes não pode ser negativo."
    if tipo_reuniao == "trabalho" or participantes > 500:
        return "Sala Grande"
    elif participantes >= 2 and participantes <= 20:
        return "Sala Pequena"
    elif participantes > 21 and participantes <= 100:
        return "Sala Média"
    elif participantes >= 501:
        return "Sala Extra Grande"
    else:
        return "Tipo de reunião inválido"
participantes = int(input("Número de participantes: "))
tipo_reuniao = input("Tipo de reunião (normal ou executiva): ").strip().lower()
print(recomendar_sala(participantes, tipo_reuniao))