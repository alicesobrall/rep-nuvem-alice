estoque = [20,15,10,30,5]
def atualizar (elemento, quantidade):
    posicao = elemento - 1
    if 0<= posicao < len(estoque):
        estoque[posicao] -= quantidade 
    else:
        print("elemento invalido!")
def exibir (estoque):
    print(f"estoque atual: {estoque}")

exibir(estoque)
atualizar(1,3)
exibir(estoque)