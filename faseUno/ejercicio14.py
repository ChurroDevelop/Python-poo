# Una farmacia aplica al precio de los remedios el 10% de descuento, hacer un programa que
# ingresando el costo de los medicamentos calcules el descuento y el precio final.

# Clase a utilizar
class Farmacia:
    def __init__(self, costo_medicamentos):
        self.costo_medicamentos = costo_medicamentos
        self.descuento = 0.10  # 10% de descuento
    def calcular_descuento(self):
        return self.costo_medicamentos * self.descuento
    def calcular_precio_final(self):
        descuento = self.calcular_descuento()
        return self.costo_medicamentos - descuento
# Datos que ingresa el usuario
costo_medicamentos = int(input("Ingrese el costo de los medicamentos en pesos: "))
# Instancia de objeto
farmacia = Farmacia(costo_medicamentos)
descuento = farmacia.calcular_descuento()
precio_final = farmacia.calcular_precio_final()
# Imprimir resultados
print(f"Costo original de los medicamentos: ${costo_medicamentos:.2f} pesos")
print(f"Descuento aplicado: ${descuento:.2f} pesos")
print(f"Precio final después del descuento: ${precio_final:.2f} pesos")