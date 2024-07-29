# Dado el valor que un cliente paga por un producto, calcular qué valor corresponde al costo total del
# producto y cuánto es el valor del IVA. Considerando que el porcentaje del IVA puede variar en el
# tiempo y de un producto a otro, este dato se lee por teclado.

# Clase a utilizar
class CalculoIVA:
    def __init__(self, valor_pago_cliente, porcentaje_iva):
        self.valor_pago_cliente = valor_pago_cliente
        self.porcentaje_iva = porcentaje_iva / 100  # Convertir el porcentaje a decimal
    def calcular_costo_total(self):
        # El valor del costo total es el valor pagado por el cliente dividido entre (1 + porcentaje de IVA)
        return self.valor_pago_cliente / (1 + self.porcentaje_iva)
    def calcular_iva(self):
        # El valor del IVA es el costo total multiplicado por el porcentaje de IVA
        costo_total = self.calcular_costo_total()
        return costo_total * self.porcentaje_iva
# Datos que ingresa el usuario
valor_pago_cliente = float(input("Introduce el valor que paga el cliente: "))
porcentaje_iva = float(input("Introduce el porcentaje de IVA: "))
# Instancia del objeto
calculo = CalculoIVA(valor_pago_cliente, porcentaje_iva)
costo_total = calculo.calcular_costo_total()
iva = calculo.calcular_iva()
# Imprimir resultados
print(f"Valor del costo total del producto: ${costo_total:.2f}")
print(f"Valor del IVA: ${iva:.2f}")