import csv

class Vehiculo:
    def __init__(self, marca, modelo, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas

    def __str__(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.ruedas} ruedas'
    
    # Devuelve una string con Atributo y Valor
    # Se puede usar en reemplazo de __str__
    def get_str(self):
        s = ""
        for att,val in vars(self).items():
            s += att.capitalize() + ": " + str(val) + ", "
        return s[:-2]

    def guardar_datos_csv(self, nom_archivo):
        try:
            with open(nom_archivo, "a", newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print(f"No existe el archivo {nom_archivo}")
        except Exception as e:
            print("Error reportado:",e)


    def  leer_datos_csv(self, nom_archivo):
        try:
            #obtener nombre del objeto
            if type(self) is type:
                nombre_clase = self.__name__
            else:
                nombre_clase = type(self).__name__

            with open(nom_archivo, "r") as archivo:
                vehiculos = csv.reader(archivo)
                print(f"Lista de Vehiculos {nombre_clase}")
                for item in vehiculos:
                    vehiculo_tipo = nombre_clase
                    if vehiculo_tipo in item[0]:
                        print(item[1])
        except FileNotFoundError:
            print(f"No existe el archivo {nom_archivo}")
        except Exception as e:
            print("Error reportado:",e)


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