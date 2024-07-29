# tres estudiantes reunieron tapas de gaseosas para repartirlas y venderlas al final del año. Martin toma
# 2/3 del total. Jairo un cuarto del total, y Lorena se queda con el resto. ¿qué parte le corresponde a
# Lorena?

# Libreria para utilizar fracciones
from fractions import Fraction
# Clase a utilizar
class DistribucionTapas:
    def __init__(self, parte_martin, parte_jairo):
        self.parte_martin = Fraction(parte_martin)
        self.parte_jairo = Fraction(parte_jairo)
    def calcular_parte_lorena(self):
        total = Fraction(1)  # Total es 1 (o 100%)
        return total - (self.parte_martin + self.parte_jairo)
# Instancia para las distribuciones
parte_martin = '2/3'
parte_jairo = '1/4'
distribucion = DistribucionTapas(parte_martin, parte_jairo)
parte_lorena = distribucion.calcular_parte_lorena()
# Imprimir resultados
print(f"La parte que le corresponde a Lorena es: {parte_lorena}")