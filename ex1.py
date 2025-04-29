negativos = 0

for reps in range(1, 8):
    numero = float(input("Digite um número: "))
    if numero < 0:
        negativos += 1
    reps += 1

if negativos > 0:
    print(f"Entre os 7 valores, {negativos} é (são) número(s) negativo(s)!")
else:
    print(f"Nenhum desses valores é negativo!")