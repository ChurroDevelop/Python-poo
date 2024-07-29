# Realice un algoritmo que a partir de proporcionarle la velocidad de un automóvil expresada en
# kilómetros por hora, proporcione la velocidad en metros por segundos.

# Clase a utilizar
class ConvertidorVelocidad:
    def __init__(self, velocidad_kmh):
        self.velocidad_kmh = velocidad_kmh
    def convertir_a_metros_por_segundo(self):
        velocidad_ms = self.velocidad_kmh * 1000 / 3600
        return velocidad_ms
# Datos que ingresa el usuario
velocidad_kmh = int(input("Ingrese los kilometros que recorre por hora: "))
# Instancia de objeto
convertidor = ConvertidorVelocidad(velocidad_kmh)
velocidad_ms = convertidor.convertir_a_metros_por_segundo()
# Imprimir resultados
print(f"Velocidad en km/h: {velocidad_kmh} km/h")
print(f"Velocidad en m/s: {velocidad_ms:.2f} m/s")