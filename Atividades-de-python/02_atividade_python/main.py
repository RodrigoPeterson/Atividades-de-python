# Import
import time
import os

try:
    # Entrada de dados
    tempo = int(input("Escreva um número qualquer: ").strip())

    # Loop
    while tempo >= 0:
        print(f"{tempo}")
        time.sleep(1)
        tempo -= 1
        os.system("cls")
except:        
    print("Contagem encerrada")
