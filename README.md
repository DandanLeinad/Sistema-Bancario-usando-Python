# Criando um Sistema Bancário

Este desafio faz parte do bootcamp da DIO, ministrado pelo professor [Guilherme Arthur de Carvalho](https://github.com/guicarvalho).

## Objetivo Geral

O objetivo é criar um sistema bancário com as operações de sacar, depositar e visualizar extrato.

## Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

### Operação de Depósito

Deve ser possível depositar valores positivos para a conta bancária. A versão 1.0.0 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o formato R$ xxx.xx.

## Versão 1.0.0

Essa é a versão inicial do sistema bancário.

## Licença

Este projeto é licenciado sob os termos da [Licença MIT](https://github.com/DandanLeinad/Sistema-Bancario-usando-Python/blob/main/LICENSE).