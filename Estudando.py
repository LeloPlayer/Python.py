#OPERADORES ARITMÉTICOS


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


#Operador 'end' utilizado para acrescentar algo no final de uma linha.
#Operador '\n' utilizado para pular uma linha em uma parte especifica do codigo.
#Operador ' : ' utilizado para escrever os espaços, podemos adicionar a quantidade de espaço que queremos no codigo, ':30' da 30 linhas de espaço.
#Operador '> Direita' e '< Esquerda' utilizado para alinhamento de caracteres, utilizamos tambem ' ^ centro ' para fazer a centralizaçao dos caracteres.

print(f'A soma é: {s}, \n o produto é {m}, \n e a divisão é {d:.3}', end = ' >>> ' ) 
print(f'A divisão inteira é {di} \n a potençia é {e}')
