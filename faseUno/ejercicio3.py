# Un programa que lea 4 números y calcule la media.
#  Media= (num1 + num2 + num3 + num4)/4

# Clase programa donde tendra sus metodos
class Programa():
    # Inicializar valores entrantes
    def __init__ (self, numUno, numDos, numTres, numCuatro):
        self.numUno = numUno
        self.numDos = numDos
        self.numTres = numTres
        self.numCuatro = numCuatro
    # Funcion media de la clase programa
    def media(self):
        return (self.numUno + self.numDos + self.numTres + self.numCuatro) / 4
# Datos que ingresa el usuario
num1 = float(input("Ingrese el numero 1: "))
num2 = float(input("Ingrese el numero 2: "))
num3 = float(input("Ingrese el numero 3: "))
num4 = float(input("Ingrese el numero 4: "))
# Instancia de un nuevo objeto de la clase programa
metodo = Programa(num1, num2, num3, num4)
# Imprimir resultados
print(f"La media de los 4 numeros es {metodo.media()}")