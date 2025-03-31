#################################### DESAFIOS #########################################


# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse Ângulo.

from math import radians, sin, cos, tan
angu = float(input('Digite o angulo que voçe deseja: '))
seno = sin(radians(angu))
print('O angulo de {} tem o SENO de {:.2f}'.format(angu, seno))

cosse = cos(radians(angu))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angu, cosse))

tange = tan(radians(angu))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angu, tange))
