class totalmetroscubicos:

    def __init__(self):
        self.__metroscubicos = float(input("Introduce los metros cubicos de la alberca: "))
        self.VALORMETROCUBICO = 10000

    def consumoDeAguaAlberca(self):
        pago = self.__metroscubicos * self.VALORMETROCUBICO
        return pago
    
pago = totalmetroscubicos()
metro = pago.consumoDeAguaAlberca()

print(f"El costo por metro cubico de agua de una alberca es?: {metro}")