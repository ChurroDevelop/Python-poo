# Un camión transporta 25 cajas de repuestos de carros. Si cada caja pesa 748 Kg ¿ Cuántos Kg
# transporta ?

# Clase a utilizar
class Camion:
    def __init__(self, peso_por_caja, num_cajas):
        self.peso_por_caja = peso_por_caja
        self.num_cajas = num_cajas
    def calcular_peso_total(self):
        return self.peso_por_caja * self.num_cajas
# Datos que ingresa el usuario
peso_por_caja = int(input("Ingrese la cantidad de kg por caja: "))
num_cajas = int(input("Ingrese la cantidad de cajas: "))
# Instancia de objeto
camion = Camion(peso_por_caja, num_cajas)
peso_total = camion.calcular_peso_total()
# Imprimir resultado
print(f"El camión transporta un total de {peso_total} Kg.")
