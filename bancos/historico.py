from datetime import datetime

# Classe Histórico.
class Historico():
    def __init__(self):
        # Atributo privado da classe Histórico.
        self.__transacoes = []

    # Decorador "@property" pode  ser acessado como um atributo de uma instância da classe Historico.
    @property
    def transacoes(self):
        return self.__transacoes
    
    # Método adicionar transação.
    def adicionar_transacao(self, transacao):
        self.__transacoes.append(
            {
                "Tipo": transacao.__class__.__name__, # Tipo de transação..
                "Valor": transacao.valor, # Valor da transação.
                "Data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"), # Data da transação (usando o módulo "datetime").
            }
        )