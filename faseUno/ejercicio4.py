# Escribir un programa que calcule el área de un triángulo:
# Base = 7 altura = 4 área del triángulo = (base * altura)/2

# Clase triangulo donde tendra sus metodos
class Triangulo():
    # Inicializar valores entrantes
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    # Funcion area de la clase triangulo
    def area(self):
        if self.base != 0 and self.altura != 0:
            return (self.base * self.altura) / 2
        else:
            return "No se puede calcular el area"
# Datos que ingresa el usuario
b = float(input("Ingrese la base del triangulo: "))
a = float(input("Ingrese la altura del triangulo: "))
# Instancia de un nuevo objeto de la clase triangulo
metodo = Triangulo(b, a)
# Imprimir resultados
print(f"El area del triangulo es: {metodo.area()}")