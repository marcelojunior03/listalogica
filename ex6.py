tabuada = int(input("De 1 a 10, escolha a tabuada que deseja analisar:\n"))

for numeros in range(1, 11):
    total = tabuada*numeros
    print(tabuada, "x", numeros, "=", total)