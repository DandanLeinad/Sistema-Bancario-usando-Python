# Define um menu com as opções disponíveis
menu = """
           Selecione uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

--> """

# Inicializa as variáveis
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal para manter o programa em execução
while True:
    # Mostra o menu e solicita uma opção ao usuário
    opcao = input(menu)

    # Opção para realizar um depósito
    if opcao == "1":
        valor_deposito = float(input("\nDigite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(f"\nDepósito: R$ {valor_deposito:.2f}")
            print(
                f"\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso!")
        else:
            print("\nValor de depósito inválido.")

    # Opção para realizar um saque
    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("\nDigite o valor a ser sacado: "))
            if 0 < valor_saque <= saldo:
                if valor_saque <= limite:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato.append(f"Saque: R$ {valor_saque:.2f}")
                    print(
                        f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso!")
                else:
                    print("\nValor de saque excede o limite diário.")
            else:
                print("\nValor de saque excede o saldo disponível.")
        else:
            print("\nLimite diário de saques atingido.")

    # Opção para mostrar o extrato
    elif opcao == "3":
        if extrato:
            print("Extrato:")
            print('\n'.join(extrato))
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("\nNão foram realizadas movimentações.")

    # Opção para sair do programa
    elif opcao == "4":
        break

    # Opção inválida
    else:
        print("\nOperação inválida. Por favor, selecione novamente a operação desejada.")
