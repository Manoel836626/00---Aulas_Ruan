


print('\n')
print('Seja Bem Vindo!')
print('Escolha uma operação:')
print('\n')
print('(a) Consulta Saldo')
print('(b) Saque')
print('(c) Depósito')
print('(d) Sair')
print('\n')


opcoes = input('Operação Ecolhida:')

saldo = 0



     
while(opcoes!='d'): # ! usado para enquanto

    if(opcoes=='a'):
        print(f'Saldo: R$ {saldo:.2f}')
    elif(opcoes=='b'):
        saque = float(input('Valor saque:'))
        saldo -= saque
        print(f'Saldo atual: R$ {saldo:.2f}')
    elif(opcoes=='c'):
        deposito = float(input('Valor depósito:'))
        saldo += deposito
        print(f'Saldo atual: R$ {saldo:.2f}')
        
    
    print('\n')
    opcao2 = input('Deseja fazer outra operação? (S/N): ')
    
    if((opcao2== 'S') or (opcao2== 's')):     
        print('\n')
        print('(a) Consulta Saldo')
        print('(b) Saque')
        print('(c) Depósito')
        print('(d) Sair')
        print('\n')
        opcoes = input('Opção Ecolhida:')  
        print(f'Saldo atual: R$ {saldo:.2f}') 
    elif ((opcao2== 'N') or (opcao2== 'n')):
        opcoes = 'd'
       
print('\n')
print('Fim')        





