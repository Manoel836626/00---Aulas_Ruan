
numero = int(input('Infome um número: '))

fatorial = numero



while (numero>1): # Enquanto contador for >= 1 executar o código
    print(fatorial,"X",numero-1)
    numero = numero-1
    fatorial = fatorial*numero

print(fatorial,"X",1)
print('Resultado: ', fatorial)