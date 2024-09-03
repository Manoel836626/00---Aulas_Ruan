sexo = (input("Informe o Sexo - (M/F):"))

altura = float(input("Informe a altura: "))

print('\n')

print ('Sexo:', sexo)


print ('Altura:', altura)

if (sexo== 'M' or sexo=='m'):
    print('Peso Ideal: ',(72.7*altura)-58)

else:
    print('Peso Ideal: ',(62.1*altura)-44.7)

print('\n')