# TODO: atividade

try:
    nome = input("Informe o seu nome: ").strip().title()
    idade = int(input("Informe sua idade: ").strip())

    #lista de filmes
    sala_1 = "A roda Quadrada"
    sala_2 = "A volta dos que não foram"
    sala_3 = "Poeira em alto mar"
    sala_4 = "As tranças do rei careca"
    sala_5 = "A vingança do frango assado"

    # Laop

    while True:
        # menu de filmes

        print(f"Sala 1 - {sala_1} - Livre")
        print(f"Sala 2 - {sala_2} - 12 anos")
        print(f"Sala 3 - {sala_3} - 14 anos")
        print(f"Sala 4 - {sala_4} - 16 anos")
        print(f"Sala 5 - {sala_5} - 18 anos")
        sala = input("Informe a sala desejada: ").strip()

    # verificação da sala selecionada

        match sala:
            case "1":
                filme = sala_1
                idade_minima = 0
            case "2":
                filme = sala_2
                idade_minima = 12
            case "3":
                filme = sala_3
                idade_minima = 14
            case "4":
                filme = sala_4
                idade_minima = 16
            case "5":
                filme = sala_5
                idade_minima = 18
            case _:
                print("Sala inexistente.")
        
        if idade >= idade_minima:
            print(f"{nome} escolheu {filme}. Tenha um bom filme!")
            break
        else:
            print(f"{nome} não foi autorizado a ver {filme}.")
            continue

except Exception as e:
    print(f"Erro no programa. {e}")