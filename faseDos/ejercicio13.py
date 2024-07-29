# Realice el siguiente algoritmo para convertir pesos a dolores y a euros, utilizando constante de valor
# de la moneda.

# Clase a utilizar
class ConvertidorMoneda:
    def __init__(self, tasa_dolar, tasa_euro):
        self.tasa_dolar = tasa_dolar
        self.tasa_euro = tasa_euro
    def convertir_a_dolares(self, pesos):
        return pesos / self.tasa_dolar
    def convertir_a_euros(self, pesos):
        return pesos / self.tasa_euro
    def mostrar_conversiones(self, pesos):
        dolares = self.convertir_a_dolares(pesos)
        euros = self.convertir_a_euros(pesos)
        # Imprimir resultados
        print(f"{pesos} pesos equivalen a ${dolares:.2f} dólares.")
        print(f"{pesos} pesos equivalen a €{euros:.2f} euros.")
# Tasas de conversión
tasa_dolar = 4500
tasa_euro = 4900
# Instancia de objeto
convertidor = ConvertidorMoneda(tasa_dolar, tasa_euro)
# Datos que ingresa el usuario
pesos = float(input("Introduce la cantidad en pesos: "))
# Mostrar las conversiones
convertidor.mostrar_conversiones(pesos)
