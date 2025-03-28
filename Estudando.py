###################################### DESAFIOS #######################################


#Faça um programa que leia a largura ea altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m**2.

print('PAREDE')

# Entrada de dados
largura = float(input('Digite a largura dessa parede (em metros): '))
altura = float(input('Digite a altura dessa parede (em metros): '))

# Cálculo da área
area = largura * altura

# Cálculo da tinta necessária (considerando 1 litro de tinta cobre 2 metros quadrados)
litros_por_metro_quadrado = 0.5  
tinta_necessaria = area * litros_por_metro_quadrado

print(f'A área da parede é de {area} metros quadrados.')
print(f'Serão necessários aproximadamente {tinta_necessaria:.2f} litros de tinta para pintar esta parede.')






