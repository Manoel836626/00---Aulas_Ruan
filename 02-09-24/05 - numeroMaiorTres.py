numeroUm = float (input('Informe o primeiro número: '))
numeroDois = float (input('Informe o segundo número: '))
numeroTres = float (input('Informe o terceiro número: '))

if (numeroUm>numeroDois and numeroUm>numeroTres):
    print('O número maior é: ',float(numeroUm))

elif (numeroDois>numeroUm and numeroDois>numeroTres):
    print('O número maior é: ',float(numeroDois)) 

else:
    print(float(numeroTres))