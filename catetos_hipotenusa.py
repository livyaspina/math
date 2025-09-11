# import math
# co = float(input("Informe o cateto oposto: "))
# ca = float(input("Informe o cateto adjacente: "))

# h = math.hypot(co, ca)
# print("A hipotenusa vai medir {:.2f}". format(h))

###################################
co = float(input("Informe o cateto oposto: "))
ca = float(input("Informe o cateto adjacente: "))
h = (co** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}". format(h))