
op = input('\nEscolha entre: \n[T]riângulo, \n[Q]uadrado, \n[R]etangulo,\n[L]osango \n[C]ícrculo:\n')

match op:
    case"T":
        print("Você escolheu Triângulo")
    case"Q":
        print("Você escolheu Quadrado")    
    case"C":
        print("Você escolheu Círculo")
    case"L":
        print("Você escolheu Losango")
    case"R":
        print("Você escolheu Retangulo")
    case default:
        print('Opção invalida') 
