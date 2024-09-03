op = input("Deseja somar?' (S/N): ")
if(op=="S" or op=="s"):
    x = int(input("Digite o primeiro numero: "))
    y = int(input("Digite o segundo numero: "))
    resultado = x+y
    print("O resultado da soma é", resultado)
    print ("Até a próxima!")
if(op=="N" or op=="n"):
    print ("Até a próxima!")