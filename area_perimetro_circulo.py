# Programa para calcular el área y el perimetro de un circulo de radio R

import math

# input
print("-------------------------------------")
R = input("Ingrese el valor del radio del círculo: ")
R = int(R)

# processing
A = math.pi*R*R
P = 2*math.pi*R

# output
print("-------------------------------------")
print("El área del circulo es: " + str(A))
print("El perímetro del circulo es: " + str(P))
print("-------------------------------------")
