




notas = []




for i in range (3):
    
    notas.append(int(input('Insira as notas: ')))

somatorio = sum(notas)


print(f'A média',{somatorio/3})