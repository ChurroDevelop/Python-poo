# Pablo compro 5 productos los dos primeros con un 5% de descuento y los 2 últimos con un 2% de
# descuento, realice un algoritmo que indique cuanto fue el valor a pagar por cada producto y el total
# de la compra.

# Clase a utilizar
class Compra:
    def __init__(self, precios):
        self.precios = precios
        self.descuentos = [0.05, 0.05, 0, 0.02, 0.02]  # Descuentos aplicables a los 5 productos
    def calcular_precios_con_descuento(self):
        precios_con_descuento = []
        for i in range(len(self.precios)):
            descuento = self.descuentos[i]
            precio_original = self.precios[i]
            precio_descuento = precio_original * (1 - descuento)
            precios_con_descuento.append(precio_descuento)
        return precios_con_descuento
    def calcular_total_compra(self):
        precios_con_descuento = self.calcular_precios_con_descuento()
        return sum(precios_con_descuento)
# Datos que ingresa el usuario
precios = []
for i in range(1, 6):
    precio = float(input(f"Introduce el precio del producto {i}: "))
    precios.append(precio)
# Instancia de objeto
compra = Compra(precios)
precios_con_descuento = compra.calcular_precios_con_descuento()
total_compra = compra.calcular_total_compra()
# Imprimir resultados
for i, precio_descuento in enumerate(precios_con_descuento, start=1):
    print(f"Precio a pagar por el producto {i}: ${precio_descuento:.2f}")
print(f"Total de la compra: ${total_compra:.2f}")