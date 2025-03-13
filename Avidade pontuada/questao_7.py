import os
os.system("clear")


nome_produto = input("Digite o nome do produto: ")
quantidade_produto = int(input("Digite a quantidade do produto: "))
preco_produto = float(input("Digite o preço do produto: "))
total = quantidade_produto * preco_produto

if quantidade_produto <= 5:
    desconto = total * 0.2
    total_a_pagar = total - desconto
    print(f"Produto: {nome_produto}  \nValor: R$ {preco_produto:.2f} \nQuantidade: {quantidade_produto} \nTotal: {total} \nDesconto: R$ {desconto:.2f} \nTotal a pagar: R$ {total_a_pagar:.2f} ")
elif quantidade_produto > 5 and quantidade_produto <= 10:
    desconto = total * 0.3
    total_a_pagar = total - desconto
    print(f"Produto: {nome_produto}  \nValor: R$ {preco_produto:.2f} \nQuantidade: {quantidade_produto} \nTotal: {total} \nDesconto: R$ {desconto:.2f} \nTotal a pagar: R$ {total_a_pagar:.2f} ")
else:
    desconto = total * 0.5
    total_a_pagar = total - desconto
    print(f"Produto: {nome_produto}  \nValor: R$ {preco_produto:.2f} \nQuantidade: {quantidade_produto} \nTotal: {total} \nDesconto: R$ {desconto:.2f} \nTotal a pagar: R$ {total_a_pagar:.2f} ")
    
