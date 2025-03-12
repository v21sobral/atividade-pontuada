import os
os.system("clear")


nome_aluno = input("Digite seu nome: ")
nota1_aluno = float(input("Digite a nota da primeira prova: "))
nota2_aluno = float(input("Digite a nota da primeira prova: "))
media_aluno = (nota1_aluno + nota2_aluno)/2


if media_aluno < 4:
    print(f" Você foi reprovado com média: {media_aluno:.1f}")
elif media_aluno >= 4 :
    print(f" Você está na recuperação com média: {media_aluno:.1f}")
elif media_aluno > 6 :
    print(f" Parabéns você foi aprovado com média: {media_aluno:.1f}")
  

