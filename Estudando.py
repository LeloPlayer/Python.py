#################################### DESAFIOS #########################################

#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimeto da hipotenusa.

from math import hypot
cateopo = float(input('Digite o comprimento do cateto oposto: ')             )
cateadja = float(input('Digite o comprimento do cateto adjacente: '))

hipo = hypot (cateopo, cateadja)

print('A hipotenusa vai medir {:.2f}'.format(hipo))