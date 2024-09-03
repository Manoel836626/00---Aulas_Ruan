
numero = int(input('Infome um número: '))

fatorial = 1

resposta = ""


for  x in range (numero,0,-1):
     
     fatorial *=x
     resposta+=str(x)
     if x>1:
        resposta+= " X "
     else:
         resposta+= " = "   

print (resposta, fatorial)


