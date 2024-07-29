# Un jefe de obra con el dinero que tiene compra cinco juegos de llaves hexagonales cada uno por
# $11500. Una bomba en $1168000 y tres cajas de pernos cada uno por $87000. Después de pagar le
# sobran $91000. ¿cuánto dinero tenía?

# Clase a utilizar
class Compra:
    def __init__(self, precio_llave, precio_bomba, precio_perno, cantidad_llaves, cantidad_pernos, dinero_restante):
        self.precio_llave = precio_llave
        self.precio_bomba = precio_bomba
        self.precio_perno = precio_perno
        self.cantidad_llaves = cantidad_llaves
        self.cantidad_pernos = cantidad_pernos
        self.dinero_restante = dinero_restante
    def calcular_costo_llaves(self):
        return self.precio_llave * self.cantidad_llaves
    def calcular_costo_bomba(self):
        return self.precio_bomba
    def calcular_costo_pernos(self):
        return self.precio_perno * self.cantidad_pernos
    def calcular_gasto_total(self):
        return (self.calcular_costo_llaves() + 
                self.calcular_costo_bomba() + 
                self.calcular_costo_pernos())
    def calcular_dinero_inicial(self):
        return self.calcular_gasto_total() + self.dinero_restante
# Datos que ingresa el usuario
precio_llave = float(input("Introduce el precio de un juego de llaves hexagonales: "))
precio_bomba = float(input("Introduce el precio de la bomba: "))
precio_perno = float(input("Introduce el precio de una caja de pernos: "))
cantidad_llaves = int(input("Introduce la cantidad de juegos de llaves hexagonales comprados: "))
cantidad_pernos = int(input("Introduce la cantidad de cajas de pernos compradas: "))
dinero_restante = float(input("Introduce el dinero restante después de las compras: "))
# Instancia de objeto
compra = Compra(precio_llave, precio_bomba, precio_perno, cantidad_llaves, cantidad_pernos, dinero_restante)
dinero_inicial = compra.calcular_dinero_inicial()
# Imprimir resultado
print(f"El dinero inicial que tenía el jefe de obra es: ${dinero_inicial:.2f}")
