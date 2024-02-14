# Variáveis globais
saldo = 0
extrato = []
limite = 500
numeros_saques = 0
usuarios = []
contas = []
LIMITE_SAQUE = 3
AGENCIA = "0001"
numero_conta = 1

# Funçao de saque
def saque(*, saldo, valor, extrato, limite, numeros_saques):
    if numeros_saques >= LIMITE_SAQUE:
        print("Limite de saques atingido.")
    else:
        if 0 < valor <= limite:
            if valor <= saldo:
                saldo -= valor
                numeros_saques += 1
                extrato.append(("Saque", valor))
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("Valor inválido para saque.")
    return saldo, extrato, numeros_saques

# Função de deposito
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(("Depósito", valor))
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")
    return saldo, extrato

# Função de exibir o extrato
def exibir_extrato(saldo, /, *, extrato):
    if extrato:
        print("\nHistórico de transações:\n")
        print("\nTipo".ljust(20), "| Valor")
        print("-" * 32)
        for tipo, valor in extrato:
            print(tipo.ljust(20), f"| R$ {valor:.2f}")
        print("-" * 32)
        print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("\nNão foram realizadas movimentações.")

# Função para criar um usuário
def criar_usuario(usuarios):
    cpf = input("\nInforme o CPF (Somente os números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nJá existe um usuário com este CPF!")
    else:
        nome = input("\nInforme o seu nome completo: ")
        data_nascimento = input(
            "\nInforme sua data de nascimento (dd/mm/aaaa): ")
        endereco = input(
            "\nInforme o seu endereço (logradouro, n° - bairro - cidade/sigla do estado): ")

        usuarios.append({
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        })
        print("\nUsuário criado com sucesso!")

# Função para filtrar um usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Função para criar uma conta
def criar_conta(AGENCIA, numero_conta, usuarios, contas):
    cpf = input("\nInforme o CPF do titular da conta (Somente os números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("\nUsuário não encontrado.")
        return

    conta = {"agencia": AGENCIA, "numero_conta": numero_conta,
             "saldo": 0, "extrato": [], "titular": usuario}
    contas.append(conta)
    print(f"\nConta criada com sucesso!\nNúmero da conta: {numero_conta}")
    return numero_conta + 1

# Função para listar as contas
def listar_contas(contas):
    if contas:
        print("\nLista de Contas:\n")
        for conta in contas:
            print(f"Agência: {conta['agencia']}")
            print(f"Número: {conta['numero_conta']}")
            print(f"Titular: {conta['titular']['nome']}\n")
    else:
        print("\nNão existem contas cadastradas.")

# Loop do menu principal
while True:
    print("\nMenu Principal:")
    print("[1] Sacar")
    print("[2] Depositar")
    print("[3] Ver extrato")
    print("[4] Nova conta")
    print("[5] Novo usuário")
    print("[6] Listar contas")
    print("[7] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor_saque = float(input("Digite o valor a ser sacado: "))
        saldo, extrato, numeros_saques = saque(
            saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numeros_saques=numeros_saques)

    elif opcao == "2":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo, extrato = deposito(
            saldo, valor_deposito, extrato)

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        numero_conta = criar_conta(
            AGENCIA=AGENCIA, numero_conta=numero_conta, usuarios=usuarios, contas=contas)

    elif opcao == "5":
        criar_usuario(usuarios=usuarios)

    elif opcao == "6":
        listar_contas(contas=contas)

    elif opcao == "7":
        break
