numeroUm  = int (input("Informe o primeiro valor: "))
numeroDois  = int (input("Informe o segundo valor: "))
numeroTres  = int (input("Informe o terceiro valor: "))

print('\n')

if  (numeroUm<numeroDois<numeroTres):
    print(numeroUm,numeroDois,numeroTres)

elif (numeroUm<numeroTres<numeroDois):
    print(numeroUm,numeroTres,numeroDois)

elif (numeroDois<numeroUm<numeroTres):
    print(numeroDois,numeroUm,numeroTres)

elif (numeroDois<numeroTres<numeroUm):
    print(numeroDois,numeroTres,numeroUm)


elif (numeroTres<numeroUm<numeroDois):
    print(numeroTres,numeroUm,numeroDois)

elif (numeroTres<numeroDois<numeroUm):
    print(numeroTres,numeroDois,numeroUm)