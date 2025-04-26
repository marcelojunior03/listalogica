import time

numero = 1
atraso = 0.5

while numero < 101:
    print(numero)

    if numero%10 == 0:
        print("Múltiplo de 10")

    time.sleep(atraso)
    numero += 1