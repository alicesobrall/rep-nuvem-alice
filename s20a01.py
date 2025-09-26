def somar(a, b):
    return a + b
 
def multiplicar(a, b):
    return a * b
 
def subtrair(a, b):
    return a - b
 
while True:
    escolha = input("Escolha a operação (+, -, *): ")
    if escolha in ('+', '-', '*'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if escolha == '+':
                print(f"{num1} + {num2} = {somar(num1, num2)}")
            elif escolha == '*':
                print(f"{num1} - {num2} = {multiplicar(num1, num2)}")
            elif escolha == '-':
                print(f"{num1} * {num2} = {subtrair(num1, num2)}")
        except ValueError as e:
            print(e)
    continuar = input("Deseja continuar calculando?[sim,nao]: ").strip().lower()
<<<<<<< HEAD:s19a01.py
    if continuar != 'nao':
        break
=======
    if continuar != 'sim':
        break
>>>>>>> e2a1ceeb3e412966014fdda29ba33ca8948ff52e:s20a01.py
