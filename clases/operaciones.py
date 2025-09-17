class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1:"))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2:"))
                break
            except Exception:
                print("Número inválido")
                continue    
    
    def sumar(self):
        self.resultado = "La suma de " + str(self.num1) + " + " + str(self.num2) + " es igula a " + str(self.num1 + self.num2)

    def restar(self):
        self.resultado = "La resta de " + str(self.num1) + " - " + str(self.num2) + " es igual a " + str(self.num1 - self.num2)

    def multiplicar(self):
        self.resultado = "La multiplicación de " + str(self.num1) + " * " + str(self.num2) + " es igual a " + str(self.num1 * self.num2)

    def dividir(self):
        self.resultado = "La división de " + str(self.num1) + " / " + str(self.num2) + " es igual a " + str(self.num1 / self.num2)
    
    def modulo(self):
        self.resultado = "El módulo de " + str(self.num1) + " % " + str(self.num2) + " es igual a " + str(self.num1 % self.num2)
        
    def mostrarResultado(self):
        print(self.resultado)
        
        