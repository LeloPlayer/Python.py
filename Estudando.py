###################################### DESAFIOS #######################################


#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('PROMOÇÃO')

#Solicita o valor do produto ao usuário
n1 = float(input('Digite o valor do produto: '))

#Calcula o valor do produto com desconto de 5%
desconto = n1 * 0.05
valor_com_desconto = n1 - desconto

#O resultado
print(f'O desconto é de R$ {desconto:.2f}')
print(f'Com o desconto, o produto sairá por R$ {valor_com_desconto:.2f}')








