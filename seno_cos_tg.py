import math 
a = float(input("Digite o ângulo que deseja: "))
s = math.sin(math.radians(a)) #converter para radians antes 
print("O ãngulo de {} tem o SENO de {:.2f}". format(a, s))
c = math.cos(math.radians(a))
print("O ãngulo de {} tem o SENO de {:.2f}". format(a, c))
t = math.tan(math.radians(a))
print("O ãngulo de {} tem o SENO de {:.2f}". format(a, t))