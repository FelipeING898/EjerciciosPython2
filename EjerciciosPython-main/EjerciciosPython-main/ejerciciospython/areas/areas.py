class areaCuadrado:

    baseTriangulo = int(input("Introduce un valor para la base del triangulo: "))
    alturaTriangulo = int(input("Introduce un valor para la altura del triangulo: "))

    baseCuadrado = int(input("Introduce un valor para la base del cuadrado: "))
    alturaCuadrado = int(input("Introduce un valor para la altura del cuadrado: "))


    def calcularVolumen(self):
        volumenTriangulo = (self.baseTriangulo * self.alturaTriangulo)/2
        volumenCuadrado = (self.alturaCuadrado * self.baseCuadrado)

        return (volumenCuadrado + volumenTriangulo)
    

# Crear una instancia de la clase
cubo = areaCuadrado()

# Calcular y mostrar el volumen
volumen = cubo.calcularVolumen()
print(f"El volumen del cubo es: {volumen}")

