
numero = int(input('Infome um número: '))

anterior = 0
proxima = 1
soma =  1


reposta = ""



for n in range (0,numero):
    
    print(anterior)
    
    soma = proxima + anterior
    anterior = proxima
    proxima = soma

     
     

  

