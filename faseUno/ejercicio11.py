# Escribir un programa que calcule el volumen de un elipsoide
# V = (4/3) * PI * a * b *c
import math
# Clase a utilizar
class Elipsoide:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calcular_volumen(self):
        volumen = (4/3) * math.pi * self.a * self.b * self.c
        return volumen
# Datos que ingresa el usuario
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
# Instancia de objeto
elipsoide = Elipsoide(a, b, c)
# Imprimir resultados
print(f"Volumen del elipsoide: {elipsoide.calcular_volumen()}")