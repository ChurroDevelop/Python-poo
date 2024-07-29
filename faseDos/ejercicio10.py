# Una empresa que contrata personal requiere determinar la edad de las personas que solicitan trabajo,
# pero cuando se les realiza la entrevista sólo se les pregunta el año en que nacieron. Realice el código
# que representen el algoritmo para solucionar este problema.
# Al final debe entregar el nombre de la persona entrevistada en mayúscula sostenida y minunscula
# sostenida y la edad del entrevistado.

# Importar libreria para el tiempo actual
from datetime import datetime
# Clase a utilizar
class Entrevista:
    def __init__(self, nombre, ano_nacimiento):
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
    def calcular_edad(self):
        ano_actual = datetime.now().year
        return ano_actual - self.ano_nacimiento
    def mostrar_informacion(self):
        edad = self.calcular_edad()
        nombre_mayus = self.nombre.upper()
        nombre_minus = self.nombre.lower()
        # Imprimir resultados
        print(f"Nombre en mayúsculas: {nombre_mayus}")
        print(f"Nombre en minúsculas: {nombre_minus}")
        print(f"Edad: {edad}")
# Datos que ingresa el usuario
nombre = input("Introduce el nombre del candidato: ")
ano_nacimiento = int(input("Introduce el año de nacimiento del candidato: "))
# Instancia de objeto
entrevista = Entrevista(nombre, ano_nacimiento)
entrevista.mostrar_informacion()
