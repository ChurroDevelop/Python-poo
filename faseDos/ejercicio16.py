# El volumen de la tierra considerado un esferoide V= 4/3= Лa2b.
# Donde a= radio ecuatorial= 6378.137 km, b= radio polar= 6353.752 km.

import math
# Clase a utilizar
class VolumenTierra:
    def __init__(self, radio_ecuatorial, radio_polar):
        self.a = radio_ecuatorial
        self.b = radio_polar
    def calcular_volumen(self):
        volumen = (4/3) * math.pi * (self.a ** 2) * self.b
        return volumen
    def mostrar_resultado(self):
        volumen = self.calcular_volumen()
        # Imprimir resultado
        print(f"El volumen de la Tierra es: {volumen:.2f} km³")
# Radios de la Tierra en kilometros
radio_ecuatorial = 6378.137
radio_polar = 6353.752
# Instancia de objeto
tierra = VolumenTierra(radio_ecuatorial, radio_polar)
# Mostrar el resultado
tierra.mostrar_resultado()
