# Import da biblioteca
import os
# Loop
while True: 
    
    # Limpeza de console
    os.system("cls")
    
    try:
        # Entrada de váriaveis
        nome = input("Digite o seu nome: ").strip().title()
        email = input("Digite o seu e-mail: ").strip().lower()
        cpf = input("Digite o seu CPF: ").strip()
        telefone = input("Digite o seu telefone: ").strip()

        # Limpeza de console
        os.system("cls")

        print(f"Nome do usuário: {nome}")
        print(f"e-mail do usuário: {email}")
        print(f"CPF do usuário: {cpf}")
        print(f"Telefone do usuário: {telefone}")

        # Menu
        print("1 - Inserir novos dados")
        print("2 - Sair")

        opcao = input("Opção desejada: ").strip()

        #verificação da opção escolhida  
        match opcao:
            case "1":
                continue
            case "2":
                break
            case _:
                print("Opção inválida")
                break
    except:
        print("Não foi possível receber informações")    