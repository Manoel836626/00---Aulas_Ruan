
numero = int(input('Informe o primeiro número: '))

numero2 = int(input('Informe o segundo número: '))



while (numero2 != numero):
    if(numero2>numero):
        print(numero2)
    elif(numero>numero2):
        print(numero)  
    numero = int(input('Informe o primeiro número: '))

    numero2 = int(input('Informe o segundo número: '))      

print('Números iguais')
