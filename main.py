menu = """
################# Sistema Bancário V1 #################

Bem-vindo de volta, cliente!

Operações:

    (d) - Depositar
    (s) - Sacar
    (e) - Extrato
    (q) - Sair

>> """

is_first_time = True

while True:
    option = input(menu if is_first_time else ">> ")
    is_first_time = False

    if option == "q":
        break
    else:
        print(">> Operação inválida <<")

print("\n>> Obrigado por usar nosso sistema, volte sempre! <<\n")
print("#######################################################")
