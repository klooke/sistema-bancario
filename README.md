# Sistema Bancário - v2
Desafio do curso ["Python para ciência de dados" da DIO](https://web.dio.me/track/potencia-tech-powered-ifood-ciencias-de-dados-com-python).

## Desafio #1:
Criar um sistema bancário com a função depósito, saque e extrato
  - [X] Conta única.
  - [X] Evitar valores negativos nas operações e saques sem saldo.
  - [X] Limite de 3 saques diário de R$ 500,00 cada.
  - [X] Valores devem está formatados, ex: R$ 0,00.

## Desafio #2:
Otimizar o sistema bancário
  - [X] - Modulariza saque, depósito e extrato.
    - [X] - Saque deve ter somente paramentos nomeados.
    - [X] - Deposito deve ter somente paramentos posicionais.
    - [X] - Extrato deve ter paramentos posicionais e nomeados.
  - [] - Criar duas novas funções: cadastrar cliente e cadastrar conta bancária.
  - [X] - Usuários devem estar em uma lista
    - [X] - Nome, Data de Nascimento, CPF (Só numeros em string e único) e Endereço.
  - [] - Contas devem estar em uma lista.
    - [] - Agencia (Fixo 0001), numero da conta (Sequencial), cpf do usuário;