# Calcular el sueldo de un empleado dados comodatos de entrada: el nombre, hrs. De trabajo y el
# pago en hora. Pagohora=15300

# Clase a utilizar
class Empleado:
    def __init__(self, nombre, horas_trabajadas):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = 15300  # Pago por hora en pesos
    def calcular_sueldo(self):
        return self.horas_trabajadas * self.pago_por_hora
# Datos que ingresa el usuario
nombre = input("Introduce el nombre del empleado: ")
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
# Instancia de objeto
empleado = Empleado(nombre, horas_trabajadas)
sueldo = empleado.calcular_sueldo()
# Imprimir resultados
print(f"Nombre del empleado: {empleado.nombre}")
print(f"Sueldo del empleado: ${sueldo:.2f} pesos")