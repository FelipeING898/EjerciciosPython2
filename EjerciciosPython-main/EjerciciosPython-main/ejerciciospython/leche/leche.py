class pagoEnGalones:

    UNGALON = 3.785
    litrosProducidos = float(input("Litro producidos: "))
    precioPorGalon = float(input("Precio por galon: "))

    def cuantoGanaPorLitros(self):
        ganancias = (self.litrosProducidos/ self.UNGALON)* self.precioPorGalon

        return ganancias
    
galon = pagoEnGalones()

ganacias = galon.cuantoGanaPorLitros()

print(f"Las ganancias en galones son: {ganacias}")

