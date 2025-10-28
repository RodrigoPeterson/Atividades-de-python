# TODO: atividades
""" 
Crie uma lista com os nomes de todos os estados brasileiros, e mostre na tela os estados em ordem alfabética

""" 
import time
import os

# Declaração de lista
estados = ["Distrito Federal", "Bahia", "Rio Grande do Sul", "Santa Catarina", "Paraná", "São Paulo", "Rio de Janeiro", "Espirito Santo", "Mato grosso do Sul", "Mato grosso", "Minas Gerais", "Goiás", "Tocantins", "Piauí", "Maranhão", "Sergipe", "Rio grande do Norte", "Pernambuco", "Paraiba", "Ceará", "Alagoas", "Amazonas", "Pará", "Roraima", "Rondonia", "Acre", "Amapá"]

# Exibição da lista em ordem alfabética

estados.sort()

os.system("cls")
print("\nOrdem alfabética:\n")

for estado in estados:
    print(estado)
    time.sleep(1)
    

# Exibição da lista em ordem alfabética reversa

estados.sort(reverse=True)

os.system("cls")
print("\nLista de estados em ordem alfabética reversa:\n")

for estado in estados:
    print(estado)
    time.sleep(1)
    
