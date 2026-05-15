num = int(input('Digite um número para o cálculo fatorial: '))
contador = num 
f = 1 

print('Calculando {}! = '.format(num), end ='')

while contador > 0:
    
    print('{} '.format(contador), end='')
    print ('x ' if contador > 1 else '= ', end='')
    f *= contador
    contador -= 1
    

print(f)