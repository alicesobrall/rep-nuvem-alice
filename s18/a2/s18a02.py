import random
total_percorrido = 0 
intervalo_n = int(input("digite o intervalo [1,1000]:"))
while intervalo_n < 1 or intervalo_n > 1001:
    intervalo_n = int(input("digite o intervalo [1,1000]:"))
distancia = 0 
for i in range(1,intervalo_n+1):
    tempo_t = random.randint(1,100)
    velocidade_v = random.randint(0,120)
    print(f"intervalo{i}|tempo_t: {tempo_t} velocidade: {velocidade_v} distancia: {tempo_t*velocidade_v}")
    distancia = tempo_t *velocidade_v
    total_percorrido += distancia 
print(f"o total percorrido em km é = {total_percorrido}")