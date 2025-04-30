reps = 1
salario = 0
soma_sal= 0
sal_baixo = 0
filhos = 0
soma_filhos = 0
pessoas = 0
maior_sal = 0

while reps == 1:
    salario = float(input("Digite o seu salário:\nR$"))
    if salario > salario:
        maior_sal == salario
    if salario <= 1000:
        sal_baixo += 1
    soma_sal += salario

    filhos = int(input("Quantos filhos(as) você tem?\n"))
    soma_filhos += filhos

    pessoas += 1

    reps = int(input("Se deseja continuar, digite 1. Se quer finalizar, digite 0:\n"))

media_sal = soma_sal/pessoas
media_filhos = soma_filhos/pessoas
porc_sal = sal_baixo/pessoas

print(f"A média salarial da população é de R${media_sal:.2f}.")
print(f"A média do número de filhos é {media_filhos:.2f}.")
print(f"O maior salário é de R${maior_sal}.") #resolver esse problema
print(f"A porcentagem de pessoas com salário de até R$1000,00 é de {porc_sal:.2%}")