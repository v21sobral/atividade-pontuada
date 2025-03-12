import os
os.system("clear")

print("""Morango                  |           Maçã       
\n2.50 kg(até 5 kg)                1.80 kg(até 5 kg)
2.20 kg(acima de 5 kg)           1.50 kg(acima de 5 kg)


""")
fruta_escolhida = input("Digite maçã ou morango: ").upper()


match fruta_escolhida:
    case "MAÇÃ":
       quantidade_fruta = int(input("Digite a quantidade comprada: "))
       resultado_maça1 = quantidade_fruta * 1.80 
       resultado_maça2 = quantidade_fruta * 1.50
       if quantidade_fruta >= 10 or resultado_maça2 > 15:
           desconto1 = (quantidade_fruta * 1.50) * 0.1
           print(f"{resultado_maça2 - desconto1}")   
       elif quantidade_fruta <= 5:   
           print(f"O valor de {quantidade_fruta} kg de maçã: {resultado_maça1} reais")
       elif quantidade_fruta > 5:
           resultado_maça1 = quantidade_fruta * 1.50
           print(f"O valor de {quantidade_fruta} kg de maçã: {resultado_maça2} reais")
    case "MORANGO":
       quantidade_fruta = int(input("Digite a quantidade comprada: "))
       resultado_morango1 = quantidade_fruta * 2.50 
       resultado_morango2 = quantidade_fruta * 2.20
       if quantidade_fruta >= 10 or resultado_morango2 > 15:
           desconto1 = (quantidade_fruta * 2.20) * 0.1
           print(f"{resultado_morango2 - desconto1}")   
       elif quantidade_fruta <= 5:   
           print(f"O valor de {quantidade_fruta} kg de maçã: {resultado_morango1} reais")
       elif quantidade_fruta > 5:
           resultado_morango1 = quantidade_fruta * 2.20
           print(f"O valor de {quantidade_fruta} kg de maçã: {resultado_morango2} reais")
       

           
        