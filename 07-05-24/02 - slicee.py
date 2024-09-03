

n1= int(input('Qual a posição Inicial: '))
n2= int(input('Qual a posição Final: '))


lista = [0]*10




for i in range(10):
   
    lista[i] = i+1



print ('Lista: ',lista)

print ('Resposta: ',lista[n1:n2+1])