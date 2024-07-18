# Escribir un programa que calcule el volumen de una esfera:
#  Radio = 3 volumen de la esfera = 4/3 * PI * radio˄3

# Importar libreria math para el manejo del PI
import math
# Clase esfera que tendra sus metodos
class Esfera():
    # Inicializar valores entrantes
    def __init__(self, radio):
        self.radio = radio
    # Funcion volumen para la clase esfera
    def volumen(self):
        if self.radio != 0:
            return (4/3) * math.pi * self.radio**3
        else:
            return "No se puede calcular el volumen de la esfera"
# Datos que ingresa el usuario
r = float(input("Ingrese el radio de la esfera: "))
# Instancia de un nuevo objeto de la clase esfera
metodo = Esfera(r)
# Imprimir resultados
print(f"El volumen de la esfera es: {metodo.volumen()}")