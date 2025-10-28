# TODO: Atividade

# Tratamento de exceção
try:
    # Entrada de dados
    nome = input("Digite seu nome: ").strip().title()
    peso = float(input("Digite seu peso atual em kg: ").strip().replace(",","."))
    altura = float(input("Digite sua altura em metros: ").strip().replace(",","."))
    imc = round(peso/altura**2,2)
    print(f"Resultado = {imc} ") # Depois do {imc} você pode colocar o ".2f" para arredondar duas casas, você está certo em usar o roud e no final colocar um ,2. Mas conheça os dois modos. Para caso de futuras manutenções.

    if imc <= 18.5:
        print(f"{nome} está só o palito")
    
    elif imc <= 24.9:
        print(f"{nome} tem o peso normal")
    elif imc <= 29.9:
        print(f"{nome} está gordo")
    elif imc <= 34.9:
        print(f"{nome} está gordão, vai treinar")
    elif imc <= 39.9:
        print(f"TA PORRA MENÓ!! {nome} ta gordão KKKKKKKKK")
    else:
        print(f"{nome} eu conheço 4 gordos e só você dá 3 deles")

except Exception as e:
    print("Erro. {e}. Tente novamente")



    #Crie um programa que receba do usuário o nome, peso (em kg) e altura (em metros), calcule o IMC do usuário (arredondado para 2 casas decimais), e exiba o diagnóstico do usuário com base na tabela do IMC.