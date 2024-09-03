
numero = int(input('Informe o primeiro número: '))

numero2 = int(input('Informe o segundo número: '))

numero3 = numero

if(numero < numero2):

    while (numero3 < numero2):
    
        print(numero3)
        numero3+=1
    print(numero2)
else:
    print('"O primeiro não pode ser maior, tente novamente"')        

