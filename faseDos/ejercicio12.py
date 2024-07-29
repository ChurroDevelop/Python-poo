# Una papelería vende libros a $10.000, cuadernos $ 7.550, y lapiceros a $5.550. Calcular el monto
# total de la venta, según la cantidad de artículos solicitados durante el día.

# Clase a utilizar
class Papeleria:
    def __init__(self, precio_libro, precio_cuaderno, precio_lapicero):
        self.precio_libro = precio_libro
        self.precio_cuaderno = precio_cuaderno
        self.precio_lapicero = precio_lapicero
    def calcular_monto_total(self, cantidad_libros, cantidad_cuadernos, cantidad_lapiceros):
        monto_libros = self.precio_libro * cantidad_libros
        monto_cuadernos = self.precio_cuaderno * cantidad_cuadernos
        monto_lapiceros = self.precio_lapicero * cantidad_lapiceros
        return monto_libros + monto_cuadernos + monto_lapiceros
# Precio constante de los articulos
precio_libro = 10000
precio_cuaderno = 7550
precio_lapicero = 5550
# Instancia de objeto
papeleria = Papeleria(precio_libro, precio_cuaderno, precio_lapicero)
# Datos que ingresa el usuario
cantidad_libros = int(input("Introduce la cantidad de libros vendidos: "))
cantidad_cuadernos = int(input("Introduce la cantidad de cuadernos vendidos: "))
cantidad_lapiceros = int(input("Introduce la cantidad de lapiceros vendidos: "))
# Calcular el monto total de la venta
monto_total = papeleria.calcular_monto_total(cantidad_libros, cantidad_cuadernos, cantidad_lapiceros)
# Imprimir resultados
print(f"El monto total de la venta es: ${monto_total:.2f}")
