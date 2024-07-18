# Escribir un programa que calcule el área de un rectángulo:
# lado1 = 3 lado2 = 4 área del rectángulo= lado1 * lado2

# Clase rectangulo que tendra sus metodos
class Rectangulo():
    # Inicializar valores entrantes
    def __init__(self, ladoUno, ladoDos):
        self.ladoUno = ladoUno
        self.ladoDos = ladoDos
    # Funcion area de la clase rectangulo
    def area(self):
        if self.ladoUno != 0 and self.ladoDos != 0:
            return self.ladoUno * self.ladoDos
        else:
            return "No se puede realizar el calculo"
# Datos que ingresa el usuario
lado1 = float(input("Ingrese el lado 1: "))
lado2 = float(input("Ingrese el lado 2: "))
# Insancia de un nuevo objeto de la clase rectangulo
metodo = Rectangulo(lado1, lado2)
# Imprimir resultados
print(f"El area del rectangulo es {metodo.area()}")