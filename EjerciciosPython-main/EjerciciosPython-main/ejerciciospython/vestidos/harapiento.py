class descuentoYprecioFinal:

    def __init__(self):
        self.__precioTraje = float(input("Precio del traje: "))
        self.DESCUENTO1 = 0.15
        self.DESCUENTO2 = 0.8

    def precioFinal(self):
        if self.__precioTraje > 2500.00:
            descuento = self.__precioTraje * self.DESCUENTO1
            precioFinal = self.__precioTraje - descuento
            print(f"El precio final del traje es de: {precioFinal} y el descuento que obtendra es de: {descuento}")
        else:
            descuento2 = self.__precioTraje * self.DESCUENTO2
            precioFinal2 = self.__precioTraje - descuento2
            print(f"El precio final del traje es de: {descuento2} y el descuento que obtendra es de: {precioFinal2}")

traje = descuentoYprecioFinal()
descuento = traje.precioFinal()

print(descuento)