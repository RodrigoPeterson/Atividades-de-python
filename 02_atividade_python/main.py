# Import
import time

# Entrada de dados
tempo = int(input("Escreva um número qualquer: "))

# Loop
while tempo > 0:
    print(f"{tempo}")
    time.sleep(1)
    tempo -= 1
    
print("Contagem encerrada")