import os
os.system("clear")

print("Some dois números e saiba se ele é maior que o terceiro")
a = float(input("Digite o segundo número que deseja somar: "))
b = float(input("Digite o segundo número que deseja somar: "))
c = float(input("Digite o terceiro número para saber se é maior ou menor que a soma: "))

soma = a + b

if soma > c:
    print(f"A soma de {a:.0f} + {b:.0f} = {soma:.0f} é maior que {c:.0f}")
elif soma < c:
    print(f"A soma de {a:.0f} + {b:.0f} = {soma:.0f} é menor que {c:.0f}")
else:
    print(f"A soma de {a:.0f} + {b:.0f} = {soma:.0f} é igual a {c:.0f}")