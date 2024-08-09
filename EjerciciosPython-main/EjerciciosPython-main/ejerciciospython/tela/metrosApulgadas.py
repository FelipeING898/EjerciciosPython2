class metroApulgadas:

    def __init__(self):
        self.__PULGADA = 0.0254
        self.__metros = float(input("Introducir valor en metros: "))

    def deMetrosApulgadas(self):
        convertir = self.__metros/ self.__PULGADA

        return convertir
    

tela = metroApulgadas()

metros = tela.deMetrosApulgadas()

print(f"El valor en pulgas es: {metros}")

