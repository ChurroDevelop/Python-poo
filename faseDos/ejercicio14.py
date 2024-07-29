# Elaborar la codificación en Python realizando el cálculo de las siguientes expresiones:
# La ecuación del movimiento unifórmenle acelerado para mostrar el efecto del desplazamiento inicial
# es la siguiente expresión: S=S0 + v0t + 1⁄2 at2
# donde:
# S= es el desplazamiento en el tiempo (m)
# v0= velocidad inicial (m/s)
# t= tiempo (seg)

# Clase a utilizar
class MovimientoUniformementeAcelerado:
    def __init__(self, desplazamiento_inicial, velocidad_inicial, aceleracion):
        self.S0 = desplazamiento_inicial
        self.v0 = velocidad_inicial
        self.a = aceleracion
    def calcular_desplazamiento(self, tiempo):
        S = self.S0 + (self.v0 * tiempo) + (0.5 * self.a * tiempo ** 2)
        return S
    def mostrar_resultado(self, tiempo):
        desplazamiento = self.calcular_desplazamiento(tiempo)
        # Imprimir resultado
        print(f"Desplazamiento (S) después de {tiempo} segundos es: {desplazamiento:.2f} metros.")
# Datos que ingresa el usuario
desplazamiento_inicial = float(input("Introduce el desplazamiento inicial (S0) en metros: "))
velocidad_inicial = float(input("Introduce la velocidad inicial (v0) en m/s: "))
aceleracion = float(input("Introduce la aceleración (a) en m/s²: "))
tiempo = float(input("Introduce el tiempo (t) en segundos: "))
# Instancia de objeto
movimiento = MovimientoUniformementeAcelerado(desplazamiento_inicial, velocidad_inicial, aceleracion)
# Mostrar el resultado
movimiento.mostrar_resultado(tiempo)
