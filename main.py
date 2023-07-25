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

user_account = dict(balance=0.00, daily_cashout_count=0, statement="")

# Positional only
def deposit(value: float, account: dict, /):
    account["balance"] += value
    account["statement"] += f"\n- Deposito: \t+ R$ {value:.2f}"
    print(f">> Deposito de R$ {value:.2f}, concluido com sucesso! consulte o extrato para mais informações. <<")

# Keyword only
def cashout(*, value: float, account: dict):
    if value > CASHOUT_LIMIT:
        print(f">> Limite por saque é de R$ {CASHOUT_LIMIT:.2f}. <<")
        return

    if value > account["balance"]:                
        print(f">> Você não tem esse valor R$ {value:.2f} em conta, consulte o extrato para mais informações. <<")
        return
    
    account["balance"] -= value
    account["daily_cashout_count"] += 1
    account["statement"] += f"\n- Saque: \t- R$ {value:.2f}"
    print(f">> Saque de R$ {value:.2f}, concluido com sucesso! consulte o extrato para mais informações. <<")

# Keyword and Positional
def statement(statement, /, *, balance):    
    print("\n################# EXTRATO #################")
    print(statement)
    print("-------------------------------------------")
    print(f"- Saldo: \t  R$ {balance:.2f}\n")

print(MENU)

while True:
    option = input(OPERATIONS)

    if option == "d":
        try:
            deposit_value = float(input(">> Digite o quanto você vai depositar: "))
            if deposit_value <= 0:
                raise ValueError
            
        except ValueError:
            print(">> Valor inválido. <<")

        else:
            deposit(deposit_value, user_account)

    elif option == "s":        
        if user_account["daily_cashout_count"] >= DAILY_CASHOUT_LIMIT:
            print(f">> Limite de saque ({DAILY_CASHOUT_LIMIT}) diário excedido. <<")
            continue
    
        try:
            cashout_value = float(input(">> Digite o quanto você vai sacar: "))
            if cashout_value <= 0:
                raise ValueError

        except ValueError:
            print(">> Valor inválido. <<")

        else:
            cashout(value=cashout_value, account=user_account)

    elif option == "e":
        statement(user_account["statement"], balance=user_account["balance"])

        input(">> Pressione qualquer tecla para continuar << ")

    elif option == "q":
        print("\n>> Obrigado por usar nosso sistema, volte sempre! <<\n")
        break
    else:
        print(">> Operação inválida <<")

print("#######################################################")
