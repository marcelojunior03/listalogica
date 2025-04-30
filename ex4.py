pessoa = 1
alturas = []
menor = 0
maior = 0

while pessoa < 16:
    coleta = float(input("Digite a altura:\n"))
    alturas.append(coleta)

    menor = min(alturas)
    maior = max(alturas)

    pessoa += 1

print(f"A menor altura é {menor:.2f}.")
print(f"A maior altura é {maior:.2f}.")