# Programa que muestre el pago de una llamada telefónica sabiendo que cada minuto cuesta $355
# pesos y un IVA de 20%.

# Clase a utilizar
class LlamadaTelefonica:
    def __init__(self, duracion_minutos):
        self.duracion_minutos = duracion_minutos
        self.costo_por_minuto = 355  # costo en pesos
        self.iva = 0.20  # 20$ del iva
    def calcular_costo_base(self):
        return self.duracion_minutos * self.costo_por_minuto
    def calcular_iva(self, costo_base):
        return costo_base * self.iva
    def calcular_costo_total(self):
        costo_base = self.calcular_costo_base()
        iva = self.calcular_iva(costo_base)
        return costo_base + iva
# Datos que ingresa el usuario
duracion = int(input("Ingrese la cantidad de minutos que demoro la llamada: "))
# Instancia de objeto
llamada = LlamadaTelefonica(duracion)
costo_total = llamada.calcular_costo_total()
# Imprimir resultados
print(f"Costo base de la llamada: ${llamada.calcular_costo_base():.2f} pesos")
print(f"IVA (20%): ${llamada.calcular_iva(llamada.calcular_costo_base()):.2f} pesos")
print(f"Costo total de la llamada: ${costo_total:.2f} pesos")