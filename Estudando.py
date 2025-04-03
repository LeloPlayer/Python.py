#######################################DESAFIOS!!###########################################

#Seu nome tem...

nome = str(input('Digite seu nome completo: '))

print('Analisando seu nome...')

print('Seu nome em maiusculas é {} '.format(nome.upper()))
print('Seu nome em minusculas é {}' .format(nome.lower()))
print('Seu nome tem {} letras' .format(len(nome) - nome.count(' ')))

separar = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(separar[0], len(separar[0])))



