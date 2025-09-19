
def somar(a, b):
    return a + b
 
def multiplicar(a, b):
    return a * b
 
def subtrair(a, b):
    return a - b

def menu():
    print ("1- Somar")
    print ("2- Multiplicar")
    print ("3- Subtrair")
 
while True:
    menu()
    escolha = int(input("Escolha a operação (1, 2, 3): ")) 
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if escolha == 1:
        print(f"{num1} + {num2} = {somar(num1, num2)}")
    elif escolha == 2:
        print(f"{num1} - {num2} = {multiplicar(num1, num2)}")
    elif escolha == 3:
        print(f"{num1} * {num2} = {subtrair(num1, num2)}")
    
    continuar = input("Deseja continuar calculando?[sim,nao]: ").lower()
    if continuar == 'nao':
        break
 
 