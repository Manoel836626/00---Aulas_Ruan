aluno = input('Escreva o nome do Aluno: ')
notaUm = float (input('Qual a primeira nota? '))
notaDois = float (input('Qual a segunda nota? '))
notatres = float (input('Qual a terceira nota? '))
media = ((notaUm + notaDois + notatres)/3)



if (notaUm< 5) or (notaDois < 5) or (notatres<5):
    print ('Reprovado')

elif (media>=6):
    print ('Aprovado')

    
else:
    print ('Reprovado')

print ('A Média do aluno é:',media)
    

        
