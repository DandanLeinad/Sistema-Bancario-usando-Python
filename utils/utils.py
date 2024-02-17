from bancos.conta import ContaCorrente
from bancos.transacao import Deposito, Saque
from clientes.pessoa_fisica import PessoaFisica
from clientes.cliente import Cliente
import textwrap

# Função filtrar cliente.
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# Função recuperar cliente.
def recuperar_conta_cliente(cliente):
    # Se o cliente não tive conta
    if not cliente.contas():
        print("\nCliente não possui conta!")
        return 

    # FIXME: não permite cliente escolher a conta
    return cliente.contas()[0]

# Função depositar.
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes) # Filtra CPF do cliente

    # Se não encontrar o cliente.
    if not cliente:
        print("\nCliente não encontrado!")
        return # Retorna para main.py

    # Se encontrar o cliente.
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)


    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

# Função sacar.
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    # Se não encontrar cliente.
    if not cliente:
        print("\nCliente não encontrado!")
        return # Retornar pro main

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

# Função de exibir extrato.
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    # Se não encontrar cliente.
    if not cliente:
        print("\nCliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['Tipo']} - {transacao['Data']}: R$ {transacao['Valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

# Função criar cliente.
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    # Se encontrar o cliente.
    if cliente:
        print("\nJá existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

# Função criar conta.
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado!")
        return

    if not isinstance(cliente, Cliente):
        print("\nO cliente encontrado não é uma instância de Cliente!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    
    if hasattr(cliente, 'contas'):
        cliente.contas().append(conta)
    else:
        cliente.contas = [conta]

    print("\n=== Conta criada com sucesso! ===")

# Função lista contas do cliente.
def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))