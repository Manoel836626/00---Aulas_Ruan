
lados = float(input("Informe a Quantidade de lados: "))

valor = float(input("Informe o valor: "))


if (lados<3):
    print('Não é um Poligono')



elif (lados==3):
    print('Triangulo')
    area = ((valor**2 )* (3**0.5))/4
    print('A area é:' ,area, "Cm²")


elif (lados==4):
    print('Quadrado')
    area = (valor*valor)
    print('A area é:' ,area,"Cm²")

elif (lados==5):
    print('Pentágono')


  
else:
    print('Poligono não identificado')
