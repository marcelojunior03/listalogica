lista = []
maior = 0
menor = 0
media = 0
reps = 1

while reps == 1:
    numeros = float(input("Digite algum valor numérico:\n"))
    
    lista.append(numeros)
    maior = max(lista)
    menor = min(lista)
    
    reps = int(input("Se deseja continuar, aperte 1. Se quer finalizar, aperte 0:\n"))

media = (maior+menor)/2

print(f"Dentre os números colocados, o maior é {maior}, o menor é {menor} e a média deles é {media:.2f}.")