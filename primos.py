

number = int(input('Digite um número: '))
total = 0 #acumulador

for n in range(1,number + 1):
    if number % n == 0:
        print('\033[33m', end='') #cor amarela
        total += 1
    else:
        print('\033[31m', end='') #cor vermelha
    print('{} '.format(n), end= '')
    
print('\n\033[0mO número {} foi divisível {} vezes.'.format(number, total))

if total == 2:
    print('É um número primo!')
else:
    print('Não é um número primo')

    
    