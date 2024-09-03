

numero = int(input('Informe o primeiro número: '))

numero2 = int(input('Informe o segundo número: '))



while (numero > numero2):
    print('O número inicial não pode ser maior que o segundo')
    numero = int(input('Informe o primeiro número: '))

    numero2 = int(input('Informe o segundo número: '))



for i in range (numero,numero2):
        
    print(numero)
        
    numero+=1


print(numero2)
