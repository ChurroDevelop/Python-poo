# Elaborar un algoritmo para calcular el promedio final de la materia de algoritmos. Dicha
# calificación se compone de los siguientes porcentajes:
# • 55% del promedio final de sus calificaciones de los tres(3) parciales.
# • 30% de la calificación examen final y
# • 15% de la calificación trabajo final.

# Clase a utilizar
class PromedioFinal:
    def __init__(self, parciales, examen_final, trabajo_final):
        self.parciales = parciales
        self.examen_final = examen_final
        self.trabajo_final = trabajo_final
    def calcular_promedio_parciales(self):
        return sum(self.parciales) / len(self.parciales)
    def calcular_promedio_final(self):
        promedio_parciales = self.calcular_promedio_parciales()
        promedio_final = (promedio_parciales * 0.55) + (self.examen_final * 0.30) + (self.trabajo_final * 0.15)
        return promedio_final
# datos que ingresa el usuario
parciales = []
for i in range(1, 4):
    calificacion = float(input(f"Introduce la calificación del parcial {i}: "))
    parciales.append(calificacion)
examen_final = float(input("Introduce la calificación del examen final: "))
trabajo_final = float(input("Introduce la calificación del trabajo final: "))
# Instancia de objeto
promedio = PromedioFinal(parciales, examen_final, trabajo_final)
promedio_final = promedio.calcular_promedio_final()
# Imprimir resultados
print(f"Promedio de parciales: {promedio.calcular_promedio_parciales():.2f}")
print(f"Promedio final de la materia: {promedio_final:.2f}")