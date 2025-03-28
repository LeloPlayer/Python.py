###################################### DESAFIOS #######################################


#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. 1 DOLAR = R$5.75 na data desse commit.

print('CARTEIRA')

# Solicita ao usuário a quantia de dinheiro que ele possui
n1 = float(input('Quanto dinheiro você tem? R$'))

# Taxa de câmbio (reais por dólar)
taxa_cambio = 5.75

# Calcula quantos dólares podem ser comprados
dolares = n1 / taxa_cambio

# Imprime o resultado
print(f'Você poderá comprar {dolares:.2f} dólares.')




