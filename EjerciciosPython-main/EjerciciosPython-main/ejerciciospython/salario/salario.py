class sueldosemanal:

    horastrabajadas = int(input("Horas Trabajadas: ")) 
    valorPorHora = float(input("Valor por hora: "))

    def calcularSueldo(self):
        sueldosemanal = (self.horastrabajadas * self.valorPorHora)

        return sueldosemanal
    
sueldo = sueldosemanal()

sueldosemana = sueldo.calcularSueldo()

print(f"El sueldo semanal es : {sueldosemana}")