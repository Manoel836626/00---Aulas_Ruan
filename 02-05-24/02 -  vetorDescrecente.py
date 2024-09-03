
n = int(input('Infome a Quantidade de notas: '))

notas = []



for i in range(n):

    notas.append (int(input('Informe o número:')))

for i in range(n-1,-1,-1):

    print (notas[i])