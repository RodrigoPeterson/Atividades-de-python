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

# biblioteca
import os 
from classes import Conta

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()
    
    cc = Conta(titular="", cpf="", n_agencia="1234-5", n_conta="3218181-1", saldo=0)

    cc.titular = input("Informe o nome do titular: ").strip().title()
    cc.cpf = input("Informe o CPF do titular: ").strip()

    limpar()

    while True:
        # menu
        print("1 - Consultar dados")
        print("2 - Depositar valor")
        print("3 - Sacar valor")
        print("4 - Sair do programa")
        opcao = input("Opção desejada: ").strip()

        match opcao:
            case "1":
                cc.consultar_dados()
                continue
            case "2":
                valor = float(input("Informe o valor do depósito: R$").strip().replace(",","."))
                print(f"Depósito efetuado com sucesso. Saldo atual: R${cc.depositar(valor):.2f}")
            case "3":
                valor = float(input("Informe o valor do saque: R$ ").strip().replace(",","."))
                print(f"Saldo atual: R$ {cc.sacar(valor)}")
                continue
            case "4":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida. Por favor tente novamente.")
                continue


if __name__== "__main__":
    main()

