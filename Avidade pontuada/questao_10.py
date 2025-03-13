import os
os.system("clear")

escolha_combustivel = input("Escolha a opção de abastecimento A-Alcool ou G-Gasolina: ").upper()

match escolha_combustivel:
    case "A":
        quantidade_litros = int(input("Quantidade de litros que deseja abastecer: "))
        if quantidade_litros <= 25:
           desconto = (quantidade_litros * 3.79) * 0.02
           valor_a_pagar = (quantidade_litros * 3.79) - desconto
           print(f"O valor a ser pago por {quantidade_litros} litros de alcool: R$ {valor_a_pagar:.2f}")
        else:
           desconto = (quantidade_litros * 3.79) * 0.04
           valor_a_pagar = (quantidade_litros * 3.79) - desconto
           print(f"O valor a ser pago por {quantidade_litros} litros de alcool: R$ {valor_a_pagar:.2f}")
    case "G":
        quantidade_litros = int(input("Quantidade de litros que deseja abastecer: "))
        if quantidade_litros <= 25:
           desconto = (quantidade_litros * 6.59) * 0.03
           valor_a_pagar = (quantidade_litros * 6.59) - desconto
           print(f"O valor a ser pago por {quantidade_litros} litros de gasolina: R$ {valor_a_pagar:.2f}")
        else:
           desconto = (quantidade_litros * 6.59) * 0.05
           valor_a_pagar = (quantidade_litros * 6.59) - desconto
           print(f"O valor a ser pago por {quantidade_litros} litros de gasolina: R$ {valor_a_pagar:.2f}")