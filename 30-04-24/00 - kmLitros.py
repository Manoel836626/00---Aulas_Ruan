
kmInicial = float (input('Informe o Km Inicial: '))
kmFinal = float (input('Informe o Km Final: '))

valorGasto = float(input('Informe o Valor Abastecido: '))
valorLitros = float(input('Informe o Valor por Litro: '))

kmPercorridos = kmFinal-kmInicial
qtdeLitros = valorGasto/valorLitros
media = kmPercorridos/qtdeLitros

print (kmPercorridos, ' percorridos.')
print (f'{qtdeLitros:.2}  abastecidos.')

print (f'{media:.2f} Kilometros por litro de combustivel.')
