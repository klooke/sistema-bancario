MENU = """################# Sistema Bancário V1 #################

Bem-vindo de volta, cliente!"""

OPERATIONS = """
Operações:

    (d) - Depositar
    (s) - Sacar
    (e) - Extrato
    (q) - Sair

>> """

print(MENU)

while True:

    option = input(OPERATIONS)
    if option == "d":
        print(">> Menu de Deposito <<")
    elif option == "s":
        print(">> Menu de Saque <<")
    elif option == "e":
        print(">> Menu de Extrato <<")
    elif option == "q":
        print("\n>> Obrigado por usar nosso sistema, volte sempre! <<\n")
        break
    else:
        print(">> Operação inválida <<")

print("#######################################################")
