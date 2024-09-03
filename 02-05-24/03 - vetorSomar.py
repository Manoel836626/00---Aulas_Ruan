
n = int(input('Infome a quantidade de numeros: '))

numeros = []

somatorio = 0
quantos = 0

for i in range(n):

    numeros.append (int(input('Informe o número:')))

for i in range(n):
        somatorio +=numeros[i]
    
        if numeros[i] >=0:
            print(numeros[i],'positivo')
            quantos= quantos+1
        else:
             print(numeros[i],'Negativo')    

print('\n')
print (quantos,'Positivos','\n')
print ('A soma é: ',somatorio)