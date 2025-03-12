import os
os.system("clear")

a = int(input("Digite o primeiro nímero: "))
b = int(input("Digite o segundo nímero: "))

if a == b:
  c =  a + b 
  print(f"{a} + {b} = {c}")
else:
  c = a * b
  print(f"{a} * {b} = {c}")


