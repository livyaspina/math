n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

med = (n1 + n2) / 2

if med >= 7:
    print("Tirando {} e {}, a média do aluno é {}".format(n1, n2, med))
    print("O aluno está APROVADO")
    
elif med > 5  and med < 6.9:
    print("Tirando {} e {}, a média do aluno é {}".format(n1, n2, med))
    print("O aluno está de RECUPERAÇÃO")

elif med < 5:
    print("Tirando {} e {}, a média do aluno é {}".format(n1, n2, med))
    print("O aluno está REPROVADO")