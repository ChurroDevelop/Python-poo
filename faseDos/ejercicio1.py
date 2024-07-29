# Se requiere calcular la distancia entre dos puntos, realizar el código que permita hallar la solución,
# por favor utilizar funciones matemáticas de Python para ello

import math
# Clase a utilizar
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distancia_a(self, otro_punto):
        # Calcular la distancia euclidiana entre self y otro_punto
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return math.sqrt(dx**2 + dy**2)
# Datos que ingresa el usuario
x1 = float(input("Introduce la coordenada x del primer punto: "))
y1 = float(input("Introduce la coordenada y del primer punto: "))
x2 = float(input("Introduce la coordenada x del segundo punto: "))
y2 = float(input("Introduce la coordenada y del segundo punto: "))
# Instancia de objetos
punto1 = Punto(x1, y1)
punto2 = Punto(x2, y2)
# Calcular la distancia entre los dos puntos
distancia = punto1.distancia_a(punto2)
# Imprimir resultados
print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia:.2f}")
