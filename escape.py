# Fórmula velocidad de escape:
# 𝑉e = raíz(2*g*r)

# importa libreria math
import math

# solicitud de inputs
radio = int(input("Ingrese radio en kilómetros:\n>"))
g = float(input("ingrese la constante g:\n>"))

# cálculo velocidad de escape del planeta
vel_escape = math.sqrt(2*g*radio*1000)

# imprimir velocidad de escape
print(f"la velocidad de escape es : {vel_escape:.1f}","[m/s]")