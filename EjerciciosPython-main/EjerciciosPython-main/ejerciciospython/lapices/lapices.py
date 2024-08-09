class costodelapices:

    def __init__(self):

        self.__cantidadDeLapices = int(input("Introduce la cantidad de lapices: "))

    def costoLapices(self):
        if self.__cantidadDeLapices > 1000:
            precio = self.__cantidadDeLapices* 85.00
            print(f"El costo de los lapices es de: {precio}")
        else: 
            precio2 = self.__cantidadDeLapices * 90
            print(f"El costo de los lapices es de: {precio2}")

costo = costodelapices()

lapices = costo.costoLapices()

print(lapices)
