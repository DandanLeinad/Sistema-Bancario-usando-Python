# Classe Pessoa Fisíca
from clientes.cliente import Cliente

# Classe Pessoa Fisíca
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco) # Chama o construtor da classe pai (Cliente)
        # Atributos privados da classe Pessoa Fisíca    
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf

    @property    
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def data_nacimento(self):
        return self.__data_nascimento