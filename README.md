# Sistema Bancário em Python

Este projeto é parte do Bootcamp da DIO, ministrado pelo professor [Guilherme Arthur de Carvalho](https://github.com/guicarvalho).

## Descrição

Um sistema bancário que controla depósitos, saques e extratos bancários

## Objetivo do desafio v3.0.0

Iniciar a modelagem do sistema bancário em POO. Adicionar classes para cliente e as operações bancárias: depósito e saque. Atualizar a implementação do sistema bancário para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML a seguir:

![Modelo de Classes UML](uml.png)


Após concluir a modelagem das classes e a criação dos métodos, atualizar os métodos que tratam as opções do menu para funcionarem com as classes modeladas.


## Estrutura do Projeto

```bash 
SISTEMA-BANCARIO-USANDO-PYTHON/
│
├── bancos/
│   ├── init.py
│   ├── conta.py
│   ├── historico.py
│   └── transacao.py
│
├── clientes/
│   ├── init.py
│   ├── cliente.py
│   └── pessoa_fisica.py
│
├── utils/
│   ├── init.py
│   ├── menu.py
│   └── utils.py
│
├── License
│
├── main.py
│
├── README.md
│
└── uml.png
```

## Conteúdo dos Arquivos

- **bancos/**: Contém os módulos relacionados às classes do banco.
    - **__init__.py**: Torna a pasta um pacote Python.
    - **conta.py**: Define a classe **`Conta`** e suas subclasses.
    - **historico.py**: Define a classe **`Historico`**.
    - **transacao.py**: Define as classes relacionadas às transações.
- **clientes/**: Contém os módulos relacionados às classes de clientes.
    - **__init__.py**: Torna a pasta um pacote Python.
    - **cliente.py**: Define a classe **`Cliente`**.
    - **pessoa_fisica.py**: Define a classe **`PessoaFisica`**.
- **utils/**: Contém módulos utilitários.
    - **__init__.py**: Torna a pasta um pacote Python.
    - **menu.py**: Contém a função **`menu()`** para exibir o menu do programa.
    - **utils.py**: Contém funções utilitárias para todo o programa.
- **LICENSE**: Licença do projeto.
- **main.py**: Arquivo principal do programa, onde a função **`main()`** é definida e o programa é iniciado.
- **README.md**: Arquivo markdown.
- **uml.png**: Imagem da UML.

## Como Usar

Para começar a utilizar o sistema bancário em Python v3.0.0, siga estas etapas:

1. **Clone o Repositório**: Você pode clonar o repositório diretamente usando o Git. Abra seu terminal ou prompt de comando e execute o seguinte comando para clonar o repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/DandanLeinad/Sistema-Bancario-usando-Python.git
    ```

    Você também pode baixar o repositório como um arquivo ZIP clicando em [este link](https://github.com/DandanLeinad/Sistema-Bancario-usando-Python/archive/refs/heads/main.zip) e extrair o arquivo em seu computador.

2. **Executando com Visual Studio Code (ou outro IDE)**: Após clonar o repositório, abra o Visual Studio Code (ou seu IDE de preferência) e navegue até o diretório do projeto que acabou de clonar. Abra o arquivo `main.py` e execute-o. Você também pode usar os comandos do Visual Studio Code para isso.

3. **Executando no Terminal**: Se preferir, você também pode executar o programa diretamente no terminal. Navegue até o diretório do projeto clonado e execute o seguinte comando:

    ```bash
    python main.py
    ```

Isso iniciará o programa e você estará pronto para começar a usar o sistema bancário em Python.


## Licença

Este projeto é licenciado sob os termos da [Licença MIT](https://github.com/DandanLeinad/Sistema-Bancario-usando-Python/blob/main/LICENSE).

## Referências

Veja mais detalhes sobre o desafio no [repositório da Digital Innovation One](https://github.com/digitalinnovationone/trilha-python-dio/tree/main/02%20-%20Programa%C3%A7%C3%A3o%20Orientada%20a%20Objetos/10%20-%20desafio).
