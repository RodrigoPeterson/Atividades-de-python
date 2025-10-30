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
    dicionario = {
        'nome': "nome", 
        'email': "email", 
        'telefone': "telefone", 
        'cpf': "cpf", 
        'genero': "genero"
        }

    nome = input("Digite o seu nome: ").strip().title()
    email = input("Digite o seu e-mail: ").strip().lower()
    telefone = input("Digite o se telefone: ").strip()
    cpf = input("Digite o seu CPF: ").strip()
    genero = input("Digite o seu genêro: ").strip()

    


except Exception as e:
    print("Algo deu errado, tente novamente {e}")