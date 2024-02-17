# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        # Atributos privados da classe Cliente
        self.__endereco = endereco
        self.__contas = []

    def contas(self):
        return self.__contas
    
    def endereco(self):
        return self.__endereco

    # Método realizar transação
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    # Método adicionar conta
    def adicionar_conta(self, conta):
        self.__contas.append(conta)