# Pinturas “La brocha gorda” requiere determinar cuánto cobrar por trabajos de pintura. Considere que
# se cobra por m2 y realice el código que representen el algoritmo que le permita ir generando
# presupuestos para cada cliente.

# Clase a utilizar
class PresupuestoPintura:
    def __init__(self, costo_por_m2):
        self.costo_por_m2 = costo_por_m2
    def calcular_presupuesto(self, area):
        return self.costo_por_m2 * area
# Datos que ingresa el usuario
costo_por_m2 = float(input("Introduce el costo por metro cuadrado de pintura: "))
area = float(input("Introduce el área a pintar (en metros cuadrados): "))
# Instancia de objeto
presupuesto = PresupuestoPintura(costo_por_m2)
costo_total = presupuesto.calcular_presupuesto(area)
# Imprimir resultado
print(f"El presupuesto para pintar un área de {area} m² es: ${costo_total:.2f}")
