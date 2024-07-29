# Un vendedor recibe un sueldo base más el 10% de comisión sobre sus ventas. Si en un mes
# cualquiera hace tres ventas por valores: v1, v2 y v3, ¿cuánto recibirá por comisión? y ¿cuánto en total
# sueldo del vendedor?.

# Clase a utilizar
class Vendedor:
    def __init__(self, sueldo_base, ventas):
        self.sueldo_base = sueldo_base
        self.ventas = ventas
        self.porcentaje_comision = 0.10  # 10% de la comision
    def calcular_comision(self):
        total_ventas = sum(self.ventas)
        return total_ventas * self.porcentaje_comision
    def calcular_sueldo_total(self):
        comision = self.calcular_comision()
        return self.sueldo_base + comision
# Datos que ingresa el usuario
sueldo_base = float(input("Introduce el sueldo base del vendedor: "))
ventas = []
for i in range(1, 4):
    venta = float(input(f"Introduce el valor de la venta {i}: "))
    ventas.append(venta)
# Instancia de objeto
vendedor = Vendedor(sueldo_base, ventas)
comision = vendedor.calcular_comision()
sueldo_total = vendedor.calcular_sueldo_total()
# Imprimir resultados
print(f"Comisión del vendedor: ${comision:.2f}")
print(f"Sueldo total del vendedor: ${sueldo_total:.2f}")