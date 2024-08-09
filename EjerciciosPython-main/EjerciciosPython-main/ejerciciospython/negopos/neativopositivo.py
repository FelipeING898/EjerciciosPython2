class esPositivoONegativo:
    def __init__(self):
        
        self.__valor1 = float(input("Introduzca cualquier valor: "))

    def determinarSiPosONeg(self):
        if self.__valor1>= 0:
            print("Valor positivo")
        else:
            print("El valor es negativo")
        
negativo = esPositivoONegativo()

positivo = negativo.determinarSiPosONeg()

print(positivo)


