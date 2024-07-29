# En el programa de cocina de “Doña Anita” han dado la receta para la preparación de bizcocho especial
# de chocolate. Por cada 100 gramos de harina hay que añadir 10 gramos de cacao y un puñado de
# nueces. Si quiero prepararlos con 20 gramos de chocolate. La cantidad de gramos de harina para
# hacer el bizcocho es?

# Clase a utiliza
class Bizcocho:
    def __init__(self, harina, cacao):
        self.harina = harina
        self.cacao = cacao
    def calcular_harina(self, cantidad_cacao):
        # Calcular la cantidad de harina necesaria para la cantidad deseada de cacao
        return (cantidad_cacao / self.cacao) * self.harina
# Crear instancia de la clase Bizcocho
harina = 100  # gramos de harina por cada 100 gramos
cacao = 10    # gramos de cacao por cada 100 gramos
bizcocho = Bizcocho(harina, cacao)
# Datos que ingresa el usuario
cantidad_cacao = float(input("Introduce la cantidad de cacao deseada (en gramos): "))
# Calcular la cantidad de harina necesaria
cantidad_harina = bizcocho.calcular_harina(cantidad_cacao)
# Imprimir el resultado
print(f"Para {cantidad_cacao} gramos de cacao, necesitas {cantidad_harina:.2f} gramos de harina.")
