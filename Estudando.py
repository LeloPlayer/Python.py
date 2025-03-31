#################################### DESAFIOS #########################################


# O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
al1 = str(input('Primeiro aluno da lista:' ))
al2 =  str(input('Segundo aluno da lista: '))
al3 =  str(input('Terceiro aluno da lista: '))
al4 =  str(input('Quarto aluno da lista: '))
al5 =  str(input('Quarto aluno da lista: '))

lista = [al1, al2, al3, al4, al5]

shuffle(lista)

print('A ordem de aprensentaçao será:')
print(lista)



