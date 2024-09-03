

numero = int(input('Infome um número: '))

divisil = 2

eprimo = True
        


if(numero==2):
    print('Número Primo')
else:    
    while (divisil<numero and eprimo): # Enquanto contador for >= 1 executar o código
        
        if(numero%divisil==0):
            eprimo = False
        divisil+=1
    if(eprimo):
        print('Número Primo')
    else:
        print('Não é um numero primo')

        
        


