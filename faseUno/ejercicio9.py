# Escribir un programa que calcule el área y el volumen de un cilindro:
# A = (2 * (PI * r˄2)) + ((2 * PI * r) * h)
# V = (PI * r2) * h
import math
# Clase a utilziar
class Cilindro:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
    def calcular_area(self):
        area_base = 2 * math.pi * self.radio ** 2
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_total = area_base + area_lateral
        return area_total
    def calcular_volumen(self):
        volumen = math.pi * self.radio ** 2 * self.altura
        return volumen
# Datos que ingresa el usuario
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))
# Instancia de un nuevo objeto
cilindro = Cilindro(radio, altura)
# Imprimir resultados
print(f"Área del cilindro: {cilindro.calcular_area()}")
print(f"Volumen del cilindro: {cilindro.calcular_volumen()}")