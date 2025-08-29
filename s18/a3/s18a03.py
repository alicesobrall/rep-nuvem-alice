qtd_corrido_c = int(input("digite a quantidade de corrida em metros[1, 10^8]: "))
while qtd_corrido_c < 1 or qtd_corrido_c > 10**8:
    qtd_corrido_c = int(input("digite a quantidade de corrida em metros[1, 10^8]: "))
tamanho_pista = int(input("digite o tamanho da pista em metros[1, 100]: "))
while tamanho_pista < 1 or tamanho_pista > 100:
    tamanho_pista = int(input("digite o tamanho da pista em metros[1, 100]: "))
ponto_termino = qtd_corrido_c % tamanho_pista
print(f"O ponto de termino é = {ponto_termino}")
