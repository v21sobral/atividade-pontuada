import os
os.system("clear")

renda_mensal = float(input("Informe sua renda mensal: "))
total_emprestimo = float(input("Informe o valor do empréstimo: "))
quantidade_parcelas = int(input("Quantidade de parcelas: "))
valor_prestacao = total_emprestimo / quantidade_parcelas

if total_emprestimo < 10 * renda_mensal and valor_prestacao < renda_mensal * 0.3 :
    print(f"O emprétimo de R$ {total_emprestimo:.2f} foi aprovado.")
else:
    print(f"O emprétimo de R$ {total_emprestimo:.2f} foi reprovado.")