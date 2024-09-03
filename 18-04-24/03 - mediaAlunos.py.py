
alunos = int(input('Qual a quantidade de Aluno: '))

alunosAtual = 1

somasNotas = 0.0

for i in range  (alunos):
    notaDoAluno = int (input('Qual a nota do aluno? '))
    
    somasNotas += notaDoAluno
    
    alunosAtual += 1
    
print('\n')
print(f'A média do Aluno é: {somasNotas/alunos:.1f}')      
print('\n')