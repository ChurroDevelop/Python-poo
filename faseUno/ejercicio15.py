# Hacer un diagrama para convertir de grados centígrados a grados Fahrenheit.

# Clase a utilizar
class ConvertidorTemperatura:
    def __init__(self, grados_centigrados):
        self.grados_centigrados = grados_centigrados
    def convertir_a_fahrenheit(self):
        grados_fahrenheit = (self.grados_centigrados * 9/5) + 32
        return grados_fahrenheit
# Datos que ingresa el usuario
grados_centigrados = int(input("Ingrese los centigrados a convertir: "))
# Instancia de objeto
convertidor = ConvertidorTemperatura(grados_centigrados)
grados_fahrenheit = convertidor.convertir_a_fahrenheit()
# Imprimir resultados
print(f"Temperatura en grados centígrados: {grados_centigrados}°C")
print(f"Temperatura en grados Fahrenheit: {grados_fahrenheit:.2f}°F")