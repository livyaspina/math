import time

p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
#time.sleep(2)
opcao = 0 
print('''
~~~~~~~~~~ OPÇÕES ~~~~~~~~~~

   [1] SOMAR
   [2] MULTIPLICAR
   [3] MAIOR
   [4] NOVOS NÚMEROS
   [5] SAIR DO PROGRAMA
   ''')

while opcao != 5:
    
   
    opcao = int(input("Qual a sua opção? "))   
    if opcao == 1:
        soma = p + s
        print('A soma de {} + {} = {}'.format(p, s, soma))
    elif opcao == 2:
        soma = p * s
        print('A multiplicação de {} X {} = {}'.format(p, s, soma))
    elif opcao == 3:
        if p > s:
            maior = p
        if s > p:
            maior = s
        print('O maior número é o {}.'.format(maior))
        
    elif opcao == 4:
        p = int(input('Primeiro valor: '))
        s = int(input('Segundo valor: '))
    
    elif opcao == 5:
        time.sleep(1)
        print('-'*35)
        print('   Fim do programa, volte sempre!')
        print('-'*35)
        
    else:
        print('Opção inválida, tente novamente!')
    


  

