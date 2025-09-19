lista=[]
while True:
    nome = input("qual o nome?[guilherme,joao,estevao]:")
    lista.append(nome)
    print(lista)
    continua = input("deseja continar?[sim,nao]: ").strip().lower()
    if continua == 'nao':
        break