
n = int(input('Infome a Quantidade de Alunos: '))

alunos = []
notas = []

listaMaior = []
notaMaiores = []

for i in range(n):
    alunos.append (input('Informe o nome do Aluno:'))  
    notas.append (float(input('Informe a nota:')))


    if notas[i] >7:
        
        listaMaior.append (alunos[i])
        notaMaiores.append (notas[i])  
print('\n')

for i in range(n):
    print(f'Aluno: {alunos[i]}')
    print(f'Nota: {notas[i]}')
print('\n')

for i in range (len(notaMaiores)):

    print ('Aluno:',listaMaior[i],'\n','Nota:',notaMaiores[i])
print('\n')      