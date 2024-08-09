class cualEsMayor:

    def __init__(self):
        self.__valor1 = float(input("Introduzca cualquier valor: "))
        self.__valor2 = float(input("Introduzca cualquier valor: "))
    
    def calcularMayorValor(self):

        if self.__valor1 > self.__valor2:
            return self.__valor1
        else:
            return self.__valor2
        
mayor = cualEsMayor()

calcularMayor = mayor.calcularMayorValor()

print(f"El valor con mayor es: {calcularMayor}")