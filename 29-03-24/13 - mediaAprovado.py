aluno = input('Escreva o nome do Aluno: ')
notaUm = float (input('Qual a primeira nota? '))
notaDois = float (input('Qual a segunda nota? '))
notatres = float (input('Qual a terceira nota? '))
media = ((notaUm + notaDois + notatres)/3)

float (input ('Média: ',media))

if (notaUm>50) and (notaDois>50) and (notatres>50) and (media<60):
     print ('Reprovado')


    
else:
    print ('Aprovado')
        
