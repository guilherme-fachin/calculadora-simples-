

#menu para o usuario
def menu():
    print("escolha uma das opcoens: ")
    print("1 - somar")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("4 - dividir")
    print("5 - sair")

#def define uma função
#Função = um bloco de código com nome, que só roda quando tu chama.
#Pensa assim:
#def menu() → “ei Python, guarda isso aí com o nome menu”
#menu() → “agora executa isso”

#funçõens basicas da calculadora
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "erro: divisao por zero"
    return a / b

#programa principal
opcao = None

#não é obrigatório ser None, mas é uma boa prática pra dizer(organizacao)
#Esses funcionam igual no teu caso:
#opcao = ""   ou   opcao = "0"   ou   opcao = None
#None só deixa mais claro o estado inicial.

while opcao != "5":
    menu()
    opcao = input("digite sua escolha: ")

    if opcao =="5":
        print("saindo da calculadora.")
        break

    if opcao in ["1","2","3","4"]:
        num1 = float(input("digite o primeiro numero: "))
        num2 = float(input("digite o segundo numero: "))
    
        if opcao =="1":
            print(f"resultado da soma: {somar(num1, num2)}")
        elif opcao =="2":
            print(f"resultado da subtração: {subtrair(num1, num2)}")
        elif opcao =="3":
            print(f"resultado da multiplicação: {multiplicar(num1, num2)}")
        elif opcao =="4":
            print(f"resultado da divição: {dividir(num1, num2)}")
    else:
        print("opcao invalida. tente novamente")
