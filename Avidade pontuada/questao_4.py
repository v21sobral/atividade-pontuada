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
           print(f"O valor de {quantidade_fruta} kg maçãs: R$ {resultado_maça2 - desconto1:.2f} .")   
       elif quantidade_fruta <= 5:   
           print(f"O valor de {quantidade_fruta} kg de maçãs: R$ {resultado_maça1:.2f} .")
       else:
           resultado_maça1 = quantidade_fruta * 1.50
           print(f"O valor de {quantidade_fruta} kg de maçã: R$ {resultado_maça2:.2f} .")
    case "MORANGO":
       quantidade_fruta = int(input("Digite a quantidade comprada: "))
       resultado_morango1 = quantidade_fruta * 2.50 
       resultado_morango2 = quantidade_fruta * 2.20
       if quantidade_fruta >= 10 or resultado_morango2 > 15:
           desconto1 = (quantidade_fruta * 2.20) * 0.1
           print(f"O valor de {quantidade_fruta} kg de morango: R$ {resultado_morango2 - desconto1:.2f} .")   
       elif quantidade_fruta <= 5:   
           print(f"O valor de {quantidade_fruta} kg de morango: R$ {resultado_morango1:.2f} .")
       else:
           resultado_morango1 = quantidade_fruta * 2.20
           print(f"O valor de {quantidade_fruta} kg de morango: R$ {resultado_morango2:.2f} .")
       

           
        