# Escribir un programa que calcule la velocidad de un proyectil que recorre 2 Km en 5 minutos. Expresar
# el resultado en metros/segundo. Velocidad = espacio/tiempo

# Clase proyectil que tendra sus metodos
class Proyectil:
    # Inicializar valores entrantes
    def __init__(self, distancia, tiempo):
        self.distancia = distancia
        self.tiempo = tiempo
    # Funcion velocidad de la clase proyectil
    def velocidad(self):
        if self.tiempo == 0:
            raise ZeroDivisionError("El tiempo no puede ser cero")
        else:
            return self.distancia / self.tiempo
# Datos que ingresa el usuario
km = float(input("Ingrese la cantidad de kilometros: "))
min = float(input("Ingrese la cantidad de minutos: "))
# Instancia de un nuevo objeto de la clase proyectil
metodo = Proyectil(km, min)
# Imprimir resultados
print(f"La velocidad del proyectil es de {metodo.velocidad():.2f} m/s")
