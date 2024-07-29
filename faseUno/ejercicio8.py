# Escribir un programa que evalúe la siguiente expresión: (a+7*c)/(b+2-a)+2*b

# Crear una nueva clase
class Expresion:
  # Inicializar valores a utilizar en la clase
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
  # Crear una funcion para evaluar la expresion del ejercicio
  def evaluar(self):
    # Manejo de errores
    try:
      resultado = (self.a + 7 * self.c) / (self.b + 2 - self.a) + 2 * self.b
    except ZeroDivisionError:
      return "Error: No es posible la division por 0"
    return resultado
# Valores que digitara el usuario
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
# Instancia de un nuevo objeto
operacion = Expresion(a, b, c)
# Imprimir resultado de la expresion
print(f"El resultado de la expresion es: {operacion.evaluar()}")