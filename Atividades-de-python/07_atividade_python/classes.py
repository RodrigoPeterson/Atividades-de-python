# TODO: atividade 07
"""
Crie um app de banco. O programa deverá ter a classe Conta, com os atributos:
4 - Titular da conta (nome)
5 - CPF do titular
6 - Número da agência
7 - Número da conta
8 - Saldo
9 O usuário irá inserir os dados "Titular da conta" e "CPF", e poderá escolher entre as seguintes opções:
- Consultar dados da conta
- Depositar valor
- Sacar valor
- Sair do programa
"""

# classes
class Conta:
    # construtor
    # é colocado dentro do parenteses o que chamamos de parâmetros
    def __init__(self, titular, cpf, n_agencia, n_conta, saldo):
        self.titular = titular
        self.cpf = cpf
        self.n_agencia = n_agencia
        self.n_conta = n_conta
        self.saldo = saldo

    def consultar_dados(self):
        print(f"Nome do titular da conta: {self.titular}")
        print(f"CPF do titular da conta: {self.cpf}")
        print(f"Agência da conta: {self.n_agencia}")
        print(f"Número da conta: {self.n_conta}")
        print(f"Saldo da conta: R${self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo 
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo
        else:
            return "Saque não permitido"
        