def recomendar_sala(participantes, tipo_reuniao):
    if participantes < 0:
        return "Número de participantes não pode ser negativo."
    if tipo_reuniao == "executiva" and participantes > 15:
        return "Sala Grande"
    elif participantes <= 5:
        return "Sala Pequena"
    elif participantes <= 15:
        return "Sala Média"
    return "Tipo de reunião inválido"
participantes = int(input("Número de participantes: "))
tipo_reuniao = input("Tipo de reunião (normal ou executiva): ").strip().lower()
print(recomendar_sala(participantes, tipo_reuniao))

