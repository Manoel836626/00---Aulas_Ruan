

nomes = []
notas = []



for i in range(2):

  n = (input('Informe o nome do Aluno:'))
  nomes.append(n)
  j = (input('Insira a nota do aluno:'))
  notas.append(j)

nossoMin = min(notas)

for i in range (2):
  if (notas[i] == nossoMin):
    print ('O aluno com a Menor nota é o:',nomes[i], ',com a nota ',min(notas))


