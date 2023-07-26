TITLE = "################# Sistema Bancário V2 #################"

LOGIN_CLIENT = """
Login:

    Digite o seu cpf de 11 dígitos para continuar, ou 'q' para sair:
"""

REG_CLIENT = """
Registro:

    CPF não cadastrado, deseja prosseguir com o cadastro? (s/n) """

LOGIN = """
Login:

    (a) - Acessar uma conta existente.
    (c) - Criar uma nova conta.
    (q) - Sair

>> """

LOGIN_ACCOUNT = """

    Para acessar uma conta digite a agencia e o numero, ex.: 0001 1, ou 'q' para sair:

>> """

OPERATIONS = """
Operações:

    (d) - Depositar
    (s) - Sacar
    (e) - Extrato
    (q) - Sair

>> """

CASHOUT_LIMIT = 500.00
DAILY_CASHOUT_LIMIT = 3

clients = []
accounts = []

def is_valid_cpf(cpf: str):
    try:
        valid_cpf = int(cpf)
        valid_cpf = list(cpf)

        if len(valid_cpf) != 11:
            raise ValueError
    
    except ValueError:
        print(">> CPF inválido. <<")
        return False
    
    return True

def list_accounts(cpf: str):
    client_accounts = [ac for ac in accounts if ac["cpf"] == cpf]

    if len(client_accounts) > 0:
        print("\nContas:\n")
        [print(f"{idx} - Ag: {ac['ag']} | Cc: {ac['num']}") for idx, ac in enumerate(client_accounts)]
    else:
        print(">> Não existe nenhuma conta cadastrada. <<")
        return None
    
    return client_accounts

def get_account(cpf: str, login_info: str):
    ag, num = login_info.split(" ")
    filter_accounts = [ac for ac in accounts if ac["cpf"] == cpf]
    client_account = [ac for ac in filter_accounts if ac["ag"] == ag and str(ac["num"]) == num]

    if len(client_account) > 0:
        return client_account[0]

def register_account(cpf: str):
    client_account = dict(ag="0001", num=len(accounts) + 1, cpf=cpf, balance=0.00, daily_cashout_count=0, statement="")
    accounts.append(client_account)
    print(f">> Nova conta criada -> Ag: {client_account['ag']} | Cc: {client_account['num']}")

def login_account(cpf: str):
    while True:
        option = input(LOGIN)

        if option == "a":
            client_accounts = list_accounts(cpf)

            if client_accounts != None:
                login_info = input(LOGIN_ACCOUNT)

                if login_info == 'q':
                    break
                
                account = get_account(cpf, login_info)
                
                if account != None:
                    return account
                else:
                    print(">> Número ou agência inválido. <<")
            
        elif option == "c":
            register_account(cpf)
        elif option == "q":
            break
        else:
            print(">> Opção inválida. <<")

def register_client(cpf: str):
    while True:
        option = input(REG_CLIENT)

        if option == "s":
            name = input("\n>> Nome: ")
            birthday = input(">> Data de nascimento: ")
            address = input(">> Endereço: ")
            client = dict(cpf=cpf, name=name, birthday=birthday, address=address)
            clients.append(client)
            print(f">> Cliente cadastrado. {client} <<")
            return client
        
        elif option == "n":
            break

        else:
            print(">> Opção inválida. <<")

def login_client():
    while True:
        print(LOGIN_CLIENT)

        user_cpf = input(">> CPF: ")

        if user_cpf == "q":
            break

        if not is_valid_cpf(user_cpf):
            continue
        
        client = [cli for cli in clients if cli['cpf'] == user_cpf]

        if len(client) <= 0:
            return register_client(user_cpf)

        return client[0]

def get_valid_input(msg: str, type):
    try:
        result = type(input(">> Digite o quanto você vai depositar: "))
        if result <= 0:
            raise ValueError
        
    except ValueError:
        print(">> Valor inválido. <<")
    
    else:
        return result

def deposit(value: float, account: dict, /):
    account["balance"] += value
    account["statement"] += f"\n- Deposito: \t+ R$ {value:.2f}"
    print(f">> Deposito de R$ {value:.2f}, concluido com sucesso! consulte o extrato para mais informações. <<")

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

def statement(statement, /, *, balance):    
    print("\n################# EXTRATO #################")
    print(statement)
    print("-------------------------------------------")
    print(f"- Saldo: \t  R$ {balance:.2f}\n")

def operate_account(user_account):
    while True:
        option = input(OPERATIONS)

        if option == "d":
            deposit_value = get_valid_input(">> Digite o quanto você vai depositar: ", float)
        
            if deposit_value != None:
                deposit(deposit_value, user_account)

        elif option == "s":        
            if user_account["daily_cashout_count"] >= DAILY_CASHOUT_LIMIT:
                print(f">> Limite de saque ({DAILY_CASHOUT_LIMIT}) diário excedido. <<")
                continue
    
            cashout_value = get_valid_input(">> Digite o quanto você vai sacar: ", float)
        
            if cashout_value != None:
                cashout(value=cashout_value, account=user_account)

        elif option == "e":
            statement(user_account["statement"], balance=user_account["balance"])

            input(">> Pressione qualquer tecla para continuar << ")

        elif option == "q":
            break

        else:
            print(">> Operação inválida <<")

if __name__ == "__main__":
    print(TITLE)
    
    client = login_client()

    if client is not None:
        account = login_account(client["cpf"])

        if account != None:
            print(TITLE)
            print(f"\nBem vindo de volta, {client['name']}!")
            print(f"\nAg.: {account['ag']} | Cc.: {account['num']}:")
            operate_account(account)
        
    print("\n>> Obrigado por usar nosso sistema, volte sempre! <<\n")
    print("#######################################################")
