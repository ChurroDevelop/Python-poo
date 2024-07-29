# Calcular la edad de una madre en el momento de dio a luz a alguno de sus hijos.

from datetime import datetime
# Clase a utilizar
class Madre:
    def __init__(self, fecha_nacimiento_madre):
        self.fecha_nacimiento_madre = datetime.strptime(fecha_nacimiento_madre, "%Y-%m-%d")
    def calcular_edad_en_nacimiento(self, fecha_nacimiento_hijo):
        fecha_nacimiento_hijo = datetime.strptime(fecha_nacimiento_hijo, "%Y-%m-%d")
        edad_en_nacimiento = fecha_nacimiento_hijo.year - self.fecha_nacimiento_madre.year - ((fecha_nacimiento_hijo.month, fecha_nacimiento_hijo.day) < (self.fecha_nacimiento_madre.month, self.fecha_nacimiento_madre.day))
        return edad_en_nacimiento
# Datos que ingresa el usuario
fecha_nacimiento_madre = input("Introduce la fecha de nacimiento de la madre (YYYY-MM-DD): ")
fecha_nacimiento_hijo = input("Introduce la fecha de nacimiento del hijo (YYYY-MM-DD): ")
# Instancia de objeto
madre = Madre(fecha_nacimiento_madre)
edad_en_nacimiento = madre.calcular_edad_en_nacimiento(fecha_nacimiento_hijo)
# Imprimir resultado
print(f"La edad de la madre en el momento del nacimiento del hijo fue: {edad_en_nacimiento} años")