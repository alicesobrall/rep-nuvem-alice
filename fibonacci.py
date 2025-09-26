def fibonacci(num_termo):
    lista = [0, 1]
    if num_termo == 0:
        lista = []
        lista.append(0)
        print(f"lista = {lista}")
    elif num_termo == 1:
        lista = []
        lista.append(0)
        lista.append(1)
        print(f"lista = {lista}")
    elif num_termo >= 2:
        for i in range(2, num_termo+1):
            proximo =  lista[-1] + lista[-2]
            lista.append(proximo)
        print(f"lista = {lista}")
    else:
        print("o numero nao e valido")

fibonacci(5)