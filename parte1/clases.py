class Vehiculo:
    def __init__(self, marca, modelo, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas

    def __str__(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.ruedas} ruedas'
    
    # Devuelve una string con Atributo y Valor
    # Es en reemplazo de __str__
    def get_str(self):
        s = ""
        for att,val in vars(self).items():
            s += att.capitalize() + ": " + str(val) + ", "
        return s[:-2]



class Automovil(Vehiculo):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return  super().__str__() + f", {self.velocidad} Km/h, {self.cilindrada} cc"

