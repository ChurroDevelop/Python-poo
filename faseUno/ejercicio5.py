# Escribir un programa que calcule la longitud y el área de una circunferencia: Radio = 4
# Longitud de la circunferencia = 2 * PI * radio
# Área de la circunferencia = PI * radio˄2

# Importar libreria math para el manejo del PI
import math
# Clase circulo que tendra sus metodos
class Circulo():
    # Inicializar valores entrantes
    def __init__(self, radio):
        self.radio = radio
    # Funcion area de la clase circulo
    def area(self):
        if self.radio != 0:
            return 2 * math.pi * self.radio
        else:
            return "No se pudo calcular el area"
    # Funcion longitud de la clase circulo
    def longitud(self):
        if self.radio != 0:
            return math.pi * self.radio**2
        else:
            return "No se puede calcular la longitud"
# Datos que ingresa el usuario
r = float(input("Ingrese el radio de la circunferencia: "))
# Instancia de un nuevo objeto de la clase circulo
metodo = Circulo(r)
# Imprimir resultados
print(f"El area de la circunferencia es: {metodo.area()} \n La longitd de la circunferencia es: {metodo.longitud()}")