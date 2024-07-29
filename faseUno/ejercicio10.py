# Escribir un algoritmo que permita obtener las raíces reales de la ecuación de segundo grado: A * x2 +
# b * x + c, siendo X un valor constante.
import math
# Clase a utilizar
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calcular_raices(self):
        discriminante = self.b ** 2 - 4 * self.a * self.c
        if discriminante > 0:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return raiz1, raiz2
        elif discriminante == 0:
            raiz_unica = -self.b / (2 * self.a)
            return raiz_unica,
        else:
            return None
# Datos que ingresa el usuario
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
# Instancia de nuevos objetos
ecuacion = EcuacionCuadratica(a, b, c)
raices = ecuacion.calcular_raices()
# Imprimir resultados
if raices:
    if len(raices) == 1:
        print(f"La ecuación tiene una raíz real: {raices[0]}")
    else:
        print(f"La ecuación tiene dos raíces reales: {raices[0]} y {raices[1]}")
else:
    print("La ecuación no tiene raíces reales")