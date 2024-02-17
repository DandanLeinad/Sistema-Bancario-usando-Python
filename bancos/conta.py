from bancos.historico import Historico
from bancos.transacao import Saque, Deposito

# Classe Conta.
class Conta:
    def __init__(self, numero, cliente):
        # Atributos privados da classe Conta.
        self.__saldo = 0
        self.__numero = numero
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico()

    # Decorador classmethod fornece uma maneira alternativa de criar uma nova instância da classe Conta. 
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    # Os métodos decorados com @property são métodos de acesso que permitem que os atributos correspondentes sejam acessados de fora da classe, mas sem permitir que eles sejam modificados diretamente.
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def historico(self):
        return self.__historico
    
    # Método sacar recebe um float e retorna um boleano.
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        # Validando se o valor é maior que o saldo.
        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        # Se o valor for maior que 0.
        elif valor > 0:
            self.__saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True
        
        # Se não for nemhuma das condiçôes.
        else:
            print("\nOperação falhou! O valor informado é inválido.")

        # Se a condição não for verdadeira.
        return False
    
    # Método depositar recebe um float e retorna um boleano.
    def depositar(self, valor):
        # Se o valor for maior que 0.
        if valor > 0:
            self.__saldo += valor
            print("\nDepósito realizado com sucesso!")
            return True

        # Se não for a outra condição.
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False
        
        # Se a condição não for verdadeira.
        return False
    
# Classe Conta Corrente que é subclasse de Conta.
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # Chama os atributos da classe pai.
        super().__init__(numero, cliente)
        # Atributos privados da classe Conta Corrente.
        self.__limite = limite
        self.__limite_saques = limite_saques

        @property
        def limite(self):
            return self.__limite
        
        @property
        def limite_saques(self):
            return self.__limite_saques
        

    # Sob escrita do método sacar.
    def sacar(self, valor):
        # Pecorre a lista de transacôes dentro da classe Historico.
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["Tipo"] == Saque.__name__]
        )

        # Variáveis
        excedeu_limite = valor > self.__limite
        excedeu_saques = numero_saques >= self.__limite_saques

        # Se excedeu o valor excedeu o limite.
        if excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")

        # Se excedeu o limite de saques.
        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")

        # Se não for nenhuma das condiçôes, retorna o método sacar da classe pai.
        else:
            return super().sacar(valor)

        # Se não for a condição "else".
        return False
    
    
    # Representação da classe Conta Corrente
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente._PessoaFisica__nome}
        """