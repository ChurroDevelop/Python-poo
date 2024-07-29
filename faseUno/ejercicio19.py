# Un estudiante realiza cuatro exámenes. Realizar el pseudocódigo que representen el algoritmo
# correspondiente para obtener el promedio de las calificaciones obtenidas. las calificaciones van 1 a 5
# puntos.

# Clase a utilizar
class Estudiante:
    def __init__(self, calificacion1, calificacion2, calificacion3, calificacion4):
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2
        self.calificacion3 = calificacion3
        self.calificacion4 = calificacion4
    def calcular_promedio(self):
        return (self.calificacion1 + self.calificacion2 + self.calificacion3 + self.calificacion4) / 4
# Datos que ingresa el usuario
calificacion1 = float(input("Introduce la calificación del examen 1 (1 a 5): "))
calificacion2 = float(input("Introduce la calificación del examen 2 (1 a 5): "))
calificacion3 = float(input("Introduce la calificación del examen 3 (1 a 5): "))
calificacion4 = float(input("Introduce la calificación del examen 4 (1 a 5): "))
# Instancia de objeto
estudiante = Estudiante(calificacion1, calificacion2, calificacion3, calificacion4)
promedio = estudiante.calcular_promedio()
# Imprimir resultados
print(f"El promedio de las calificaciones es: {promedio:.2f}")