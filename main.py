MENU = """################# Sistema Bancário V1 #################

Bem-vindo de volta, cliente!"""

OPERATIONS = """
Operações:

    (d) - Depositar
    (s) - Sacar
    (e) - Extrato
    (q) - Sair

>> """

CASHOUT_LIMIT = 500.00
DAILY_CASHOUT_LIMIT = 3

balance = 0.00
daily_cashout_count = 0
statement = ""

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
            statement += f"\n- Deposito: \t+ R$ {deposit:.2f}"
            print(f">> Deposito de R$ {deposit:.2f}, concluido com sucesso! consulte o extrato para mais informações. <<")

    elif option == "s":
        
        if daily_cashout_count >= DAILY_CASHOUT_LIMIT:
            print(f">> Limite de saque ({DAILY_CASHOUT_LIMIT}) diário excedido. <<")
            continue
        
        cashout = 0.00
        try:
            cashout = float(input(">> Digite o quanto você vai sacar: "))
            if cashout <= 0:
                raise ValueError
            
            if cashout > CASHOUT_LIMIT:
                print(f">> Limite por saque é de R$ {CASHOUT_LIMIT:.2f}. <<")
                continue

            if cashout > balance:                
                print(f">> Você não tem esse valor R$ {cashout:.2f} em conta, consulte o extrato para mais informações. <<")
                continue

        except ValueError:
            print(">> Valor inválido. <<")

        else:
            balance -= cashout
            daily_cashout_count += 1
            statement += f"\n- Saque: \t- R$ {cashout:.2f}"
            print(f">> Saque de R$ {cashout:.2f}, concluido com sucesso! consulte o extrato para mais informações. <<")

    elif option == "e":
        print("\n################# EXTRATO #################")
        print(statement)
        print("-------------------------------------------")
        print(f"- Saldo: \t  R$ {balance:.2f}\n")
        
        input(">> Pressione qualquer tecla para continuar << ")

    elif option == "q":
        print("\n>> Obrigado por usar nosso sistema, volte sempre! <<\n")
        break
    else:
        print(">> Operação inválida <<")

print("#######################################################")
