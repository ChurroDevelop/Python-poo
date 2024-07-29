# Leer el sistema de ecuaciones lineales e imprimir su solución sabiendo que:
# ax + by =c
# dx + ey =f
# siendo x= (CC-bf)/(ae-db) y= (af-cd)/(ae-db)

# Clase a utilizar
class SistemaEcuaciones:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def resolver_ecuaciones(self):
        denominador = (self.a * self.e - self.b * self.d)
        if denominador == 0:
            raise ValueError("El denominador es cero, el sistema no tiene solución única.")
        x = (self.c * self.e - self.b * self.f) / denominador
        y = (self.a * self.f - self.c * self.d) / denominador
        return x, y
    def mostrar_resultado(self):
        x, y = self.resolver_ecuaciones()
        # Imprimir resultados
        print(f"Solución del sistema:")
        print(f"x = {x:.2f}")
        print(f"y = {y:.2f}")
# Datos que inresa el usaurio
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el término independiente c: "))
d = float(input("Introduce el coeficiente d: "))
e = float(input("Introduce el coeficiente e: "))
f = float(input("Introduce el término independiente f: "))
# Instancia de objeto
sistema = SistemaEcuaciones(a, b, c, d, e, f)
# Mostrar la solución
sistema.mostrar_resultado()
