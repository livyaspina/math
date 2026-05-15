

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for p in range(len(junto) -1, -1, -1):
    inverso += junto[p]

print('A frase {} ao contrário é {}'.format(junto, inverso))

if junto == inverso:
    print('É UM PALÍDROMO')
else:
    print('NÃO É UM PALÍNDROMO')