total = 0

for numero in range(1, 501):
    if numero%2 != 0 and numero%3 == 0:
        total += numero
print(total)