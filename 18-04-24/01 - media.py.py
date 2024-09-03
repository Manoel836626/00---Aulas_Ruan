
qteValores = int (input('Qual a quantidade de Valores: '))


somaValores = 0
x=0

for i in range (qteValores):
    valor = float (input('Informe o valor:'))

    somaValores += valor
    
    
print('\n')
print('A média de Valores é: ',somaValores/qteValores)      
print('\n')
  