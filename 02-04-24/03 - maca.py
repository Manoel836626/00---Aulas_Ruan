qtdeMaca = float(input("Quantas Maçãs? "))



if float(qtdeMaca>=12):
    print('Maças Compradas: ',qtdeMaca)
    print('Valor unitário: R$ 0,25')
    print('Valor Total é: R$',float(qtdeMaca*0.25))

else:
    print('Maças Compradas: ',qtdeMaca)
    print('Valor unitário: R$0,30')
    print('Valor Total é: R$',float(qtdeMaca*0.30))
