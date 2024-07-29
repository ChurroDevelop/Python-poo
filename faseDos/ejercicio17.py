# Calcular la calificación final de un aprendiz en el curso de fundamentos programación.
# Donde las evaluaciones tienen los siguientes porcentajes:
# 40% 2 exámenes
# 30% 2 trabajos
# 20% tareas y trabajos
# 10% proyecto final

# Clase a utilizar
class CalificacionFinal:
    def __init__(self, examenes, trabajos, tareas, proyecto_final):
        self.examenes = examenes
        self.trabajos = trabajos
        self.tareas = tareas
        self.proyecto_final = proyecto_final
    def calcular_calificacion_final(self):
        # Calcular promedios de las evaluaciones
        promedio_examenes = sum(self.examenes) / len(self.examenes)
        promedio_trabajos = sum(self.trabajos) / len(self.trabajos)
        # Aplicar los porcentajes a los promedios
        calificacion_final = (
            (0.40 * promedio_examenes) +
            (0.30 * promedio_trabajos) +
            (0.20 * self.tareas) +
            (0.10 * self.proyecto_final)
        )
        return calificacion_final
    def mostrar_resultado(self):
        calificacion_final = self.calcular_calificacion_final()
        # Imprimir resultados
        print(f"La calificación final del aprendiz es: {calificacion_final:.2f}")
# Datos que ingresa el usuario
examen1 = float(input("Introduce la calificación del primer examen: "))
examen2 = float(input("Introduce la calificación del segundo examen: "))
trabajo1 = float(input("Introduce la calificación del primer trabajo: "))
trabajo2 = float(input("Introduce la calificación del segundo trabajo: "))
tareas = float(input("Introduce la calificación de tareas y otros trabajos: "))
proyecto_final = float(input("Introduce la calificación del proyecto final: "))
# Instancia de objeto
calificacion = CalificacionFinal(
    examenes=[examen1, examen2],
    trabajos=[trabajo1, trabajo2],
    tareas=tareas,
    proyecto_final=proyecto_final
)
# Mostrar la calificación final
calificacion.mostrar_resultado()
