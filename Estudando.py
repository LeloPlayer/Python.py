#################################### DESAFIOS #########################################

# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela sua porçao inteira
# Exemplo: Digite 6.127 o numero tem que apareçer a parte inteira 6.

from math import trunc

num = float(input('Digite um numero Real: '))
print('A parte inteira do numero {} é {}'.format(num, trunc(num)))















