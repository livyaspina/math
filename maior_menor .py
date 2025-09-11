a = int(input("primeiro valor: "))
b = int(input("segundo o valor: "))
c = int(input("terceiro o valor: "))

menor = a 
# if a < b and a < c: "segunda forma de usar"
#     menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    
maior = a
# if a > b and a > c:  "segunda forma de usar"
#     maior = a
if b > a and b > c:
    maior = b 
if c > a and c > b:
    maior = c 
    
print("O menor número é o {}".format(menor))
print("O maior número é o {}".format(maior))
