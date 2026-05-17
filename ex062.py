print('GERADOR DE PA')
print('-='*10)

p = int(input('1º termo: '))
r = int(input('Razão da PA: '))

termo = p
contador = 1
total = 0 
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        contador += 1     
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))

print('Progressão finalizada com {} termos mostrados'.format(total))
    


