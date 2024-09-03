massaMascular = float (input('Informe a massa mascular: '))
altura = float (input('Informe a altura: '))

imc = float(massaMascular/(altura*altura))


print('O imc é: ',imc)

if (imc<18.5):
    print('Abaixo do peso')
elif (imc>=18.5 and imc<25):
    print('Saudável')    
elif (imc>=25 and imc<30):
    print('Peso em Excesso')
elif (imc>=30 and imc<35):
    print('Obesidade Grau II (severa)')
elif (imc>=40):
    print('Obesidade Grau III (mórbida)')           