
# Entrada de dados
nome = input("Digite seu nome: ").strip().title()
peso = float(input("Digite seu peso atual: ").strip().replace(",","."))
altura = float(input("Digite sua altura: ").strip().replace(",","."))
imc = round(peso/altura**2,2)
print(f"Resultado = {imc}")

if imc <= 18.5:
    print("Você está abaixo do peso")
elif imc <= 24.9:
    print("Você tem o peso normal")
elif imc <= 29.9:
    print("Você está gordo")
elif imc <= 34.9:
    print("Você está gordão, vai treinar")
elif imc <= 39.9:
    print("TA PORRA MENÓ!!")
else:
    print("Eu conheço 4 gordos e só você dá 3 deles")