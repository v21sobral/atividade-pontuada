import os
os.system("clear")

nome_usuario = input("Digite seu nome: ")
sexo = input("Digite seu sexo M(Masculino) e F(Feminino) : ").upper()
estado_civil = input("Digite seu estado civil S(Solterio(a)) C(Casado(a)) V(Viúvo(a): ").upper()

if sexo == "F" and estado_civil == "C":
    anos = input("Digite seus anos de casada: ")
    print(f"Sra.:{nome_usuario} \nSexo:{sexo} \nTem {anos} anos de idade.")
else:
    print(f"Sr(a).:{nome_usuario} \nSexo:{sexo}")
