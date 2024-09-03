

tamanhoLista = 5
lista = []

for i in range (tamanhoLista):
    lista.append(int(input("Digite um núemero")))

numeroPesquisado = int(input("Digite o número que deseja pesquisar: "))

posicaoDoNumeroPesquisado = -1

for i in range(tamanhoLista):
    if lista[i] == posicaoDoNumeroPesquisado:
        posicaoDoNumeroPesquisado = 1
        break
print()    