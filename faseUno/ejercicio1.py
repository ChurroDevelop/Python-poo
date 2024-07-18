# Escribir un programa que sume, reste, multiplique y divida dos números 

# Clase calculadora donde tendra todos los metodos
class Calculadora():
    # Inicializar valores entrantes
    def __init__(self, numUno, numDos):
        self.numUno = numUno
        self.numDos = numDos
    # Funcion sumar de la clase calculadora
    def sumar(self):
        return self.numUno + self.numDos
    # Funcion restar de la clase calculadora
    def restar(self):
        return self.numUno - self.numDos
    # Funcion multiplicar de la clase calculadora
    def multiplicar(self):
        return self.numUno * self.numDos
    # Funcion dividir de la clase calculadora
    def dividir(self):
        if self.numDos != 0:
            return self.numUno / self.numDos
        else:
            return "No se puede realizar division por 0"
# Datos que ingresa el usuario
num1 = float(input("Ingrese el numero 1: "))
num2 = float(input("Ingrese el numero 2: "))
# Instancia de un nuevo objeto de la clase calculadora
metodos = Calculadora(num1, num2)
# Imprimir resultados
print(f"El resultado de la suma es {metodos.sumar()} \n El resultado de la resta es {metodos.restar()} \n El resultado de la multiplicacion es {metodos.multiplicar()} \n El resultado de la division es {metodos.dividir()}")