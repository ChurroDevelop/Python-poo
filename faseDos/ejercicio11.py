# Ingrese una frase que lo identifique como programador de Software y luego mostar esta frase
# invertida.

# Clase a utilizar
class FraseInvertida:
    def __init__(self, frase):
        self.frase = frase
    def invertir_frase(self):
        # Invertir la frase utilizando el slicing
        return self.frase[::-1]
    def mostrar_frase_invertida(self):
        frase_invertida = self.invertir_frase()
        # Imprimir resultados
        print(f"Frase original: {self.frase}")
        print(f"Frase invertida: {frase_invertida}")
# Frase que ingresa el usuario
frase = input("Introduce una frase que te identifique como programador de software: ")
# Instancia de objeto
frase_invertida = FraseInvertida(frase)
frase_invertida.mostrar_frase_invertida()
