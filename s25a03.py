vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]
def calcular_venda_mensal (venda_mensais):
    resultado = 0
    for qtd_produto in vendas_mensais : 
        resultado += qtd_produto
    return resultado
print(f"total vendas : {calcular_venda_mensal (vendas_mensais)}")
def media_mensal