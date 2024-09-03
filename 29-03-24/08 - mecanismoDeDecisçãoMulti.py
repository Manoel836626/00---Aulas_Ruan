op = input("Deseja somar (S) ou Multi (M)'?: ")

x = int(input("Digite o primeiro numero: "))
y = int(input("Digite o segundo numero: "))

if(op=="S" or op=="s"):
    resultado = x+y

else:
    resultado = x*y

print("O resultado da soma é", resultado)
print ("Até a próxima!")
