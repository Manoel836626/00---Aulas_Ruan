

dia = input('Informe o dia da Semana: ')

lista = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado']

posicao = lista.index(dia)

print(lista[posicao+1::])