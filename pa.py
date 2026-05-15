primeiro_termo = int(input('Primeiro termo: '))
razao = int(input("Razão: "))
decimo = primeiro_termo + (11-1) * razao

for r in range(primeiro_termo, decimo, razao):
    print('{}'.format(r), end=' -> ')
print('ACABOU!')
