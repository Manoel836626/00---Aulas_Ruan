
n = int(input('Informe a quantidade de notas: '))

notas = []



for i in range(n):

    notas.append (float(input('Informe a nota:')))

notas.sort()
notasMaiores = notas[-3::]
print (notas)
print (notasMaiores)

print (f'A Média é: {(sum(notasMaiores)/3):.1f}')
