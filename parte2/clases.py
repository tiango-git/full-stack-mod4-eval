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


class Particular(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada, puestos):
        super().__init__(marca, modelo, ruedas, velocidad, cilindrada)
        self.puestos = puestos

    def get_puestos(self):
        return self.puestos
    
    def set_puestos(self, puestos_new):
        self.puestos = puestos_new

    def __str__(self):
        return  super().__str__() + f", Puestos: {self.puestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, ruedas, velocidad, cilindrada)
        self.carga = carga

    def get_carga(self):
        return self.carga
    
    def set_carga(self, carga_new):
        self.carga = carga_new

    def __str__(self):
        return  super().__str__() + f", Carga: {self.carga} Kg"
    

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, ruedas, tipo):
        super().__init__(marca, modelo, ruedas)
        self.tipo = tipo

    def __str__(self):
        return  super().__str__() + f", Tipo: {self.tipo}"
    

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return  super().__str__() + f", Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"