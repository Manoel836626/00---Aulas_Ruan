

numero = int(input('Informe um número: '))

somatorio = 0

resposta = ""
qtdeNumeros = 0
for i in range (1,numero):
    
    if(numero%i==0):
        somatorio +=i
        qtdeNumeros +=1
        if(qtdeNumeros>1):
            resposta +='+'+str(i)
        else:
            resposta +=str(i)    
      
print('\n')
if(somatorio==numero):
    print("Número perfeito")
    print(f'{resposta} = {numero}')
else:
    print("Não é um numero perfeito")            

