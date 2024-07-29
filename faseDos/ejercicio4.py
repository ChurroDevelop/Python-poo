  # Generar el algoritmo que dé como resultado el tiempo estimado para el llenado de un depósito.
  # Q=V/t, siendo Q (caudal), V (volumen) y t (tiempo).
  # Volumen = PI *(radio^2)* H (altura del depósito)
  # El tiempo se encuentra en minutos.
  # Normalmente se mide el volumen en litros y el tiempo en segundos.

import math
# Clase que se va a utilizar
class Deposito:
    def __init__(self, r, h, q):
        self.r = r
        self.h = h
        self.q = q
    def calc_volumen(self):
        # Calcular el volumen del depósito en litros
        return math.pi * (self.r ** 2) * self.h
    def calc_tiempo(self):
        # Calcular el tiempo en segundos para llenar el depósito
        vol = self.calc_volumen()
        return vol / self.q
    def calc_tiempo_min(self):
        # Convertir el tiempo de segundos a minutos
        return self.calc_tiempo() / 60
# Datos que ingresa el usuario
radio = float(input("Introduce el radio del depósito (en metros): "))
altura = float(input("Introduce la altura del depósito (en metros): "))
caudal = float(input("Introduce el caudal de llenado (en litros por segundo): "))
# Instancia de objeto
dep = Deposito(radio, altura, caudal)
tiempo_min = dep.calc_tiempo_min()
# Imprimit resultados
print(f"Tiempo estimado para llenar el depósito: {tiempo_min:.2f} minutos")
