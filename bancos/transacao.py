# Esses são usados para definir classes e métodos abstratos.
from abc import ABC, abstractproperty, abstractclassmethod

# Classe abstrata Transação.
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

# Classe Saque que é subclasse de Transação.
class Saque(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    # Método registrar chama o método sacar da Classe Conta.
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor) # Chama o método sacar da classe Conta.
        
        # Amarzena a transação no histórico da conta (self).
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Classe Depósito que é subclasse de Transação.   
class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor) # Chama o método depositar da classe Conta.

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)