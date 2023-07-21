MENU = """################# Sistema Bancário V1 #################

Bem-vindo de volta, cliente!"""

OPERATIONS = """
Operações:

    (d) - Depositar
    (s) - Sacar
    (e) - Extrato
    (q) - Sair

>> """

balance = 0.00

print(MENU)

while True:

    option = input(OPERATIONS)
    if option == "d":
        
        try:
            deposit = float(input(">> Digite o quanto você vai depositar: "))
            if deposit <= 0:
                raise ValueError
            
        except ValueError:
            print(">> Valor inválido. <<")

        else:
            balance += deposit
            print(f">> Deposito de R$ {deposit:.2f}, concluido com sucesso! <<")

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
