# TODO: atividade
"""

Crie um programa que receba do usuário os seguintes dados:
- Nome
- E-mail
- Telefone
- CPF
- Gênero

Após isso, o programa deve armazenar esses dados em um dicionário e exibir os dados desse dicionário na tela.

"""

try:
    
    dicionario = {}


    dicionario['nome'] = input("Digite o seu nome: ").strip().title()
    dicionario['email'] = input("Digite o seu e-mail: ").strip().lower()
    dicionario['telefone'] = input("Digite o se telefone: ").strip()
    dicionario['cpf'] = input("Digite o seu CPF: ").strip()
    dicionario['genero'] = input("Digite o seu genêro: ").strip().capitalize()

    print("\nDados do usuário: \n")

    for chave in dicionario:
        print(f"{chave.capitalize()}: {dicionario[chave]}")


except Exception as e:
    print(f"Algo deu errado, tente novamente {e}")