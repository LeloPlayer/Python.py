###################################### DESAFIOS #######################################


#Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

print('TABUADA')

n1 = int(input('Digite um numero: '))

print(f'TABUADA DO {n1}:')

for i in range(1, 11):
    print(f'{n1} x {i} = {n1 * i}')


