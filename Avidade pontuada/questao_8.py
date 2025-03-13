import os
os.system("clear")

cor_cd = input("Digite a cor do cd para saber o preço: ").upper()

match cor_cd:
    case "VERDE":
        verde = 10.00
        print(f"CD Verde no valor: R$ {verde:.2f}" )
    case "AZUL":
        azul = 20.00
        print(f"CD Azul no valor: R$ {azul:.2f}" )
    case "AMARELO":
        amarelo = 20.00
        print(f"CD Amarelo no valor: R$ {amarelo:.2f}" )
    case "VERMELHO":
        vermelho = 40.00
        print(f"CD Vemelho no valor: R$ {vermelho:.2f}" )
