
alunos = int(input('Qual a quantidade de Aluno: '))

alunosAtual = 1

somasNotas = 0.0

while (alunosAtual <= alunos):
    notaDoAluno = float(input('Qual a nota do aluno? '))
    
    somasNotas += notaDoAluno
    
    alunosAtual += 1
    
print('\n')
print('A média da sala é: ',somasNotas/alunos)      
print('\n')
  