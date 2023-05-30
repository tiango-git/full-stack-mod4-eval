class Vehiculo:
    def __init__(self, marca, modelo, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas

    # Devuelve una string con Atributo y Valor
    def __str__(self):
        s = ""
        for att,val in vars(self).items():
            s += att.capitalize() + ": " + str(val) + ", "
        return s[:-2]

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada



# Obtener lista de los nombres de los atributos
atributos = list(Automovil.__init__.__code__.co_varnames)[1:]

instancias = {}

# Pedir los datos y guardarlos
cantidad = int(input("Cuantos vehículos desea insertar: "))
for i in range(1,cantidad+1):
    print(f"\nDatos del automóvil {i}")
    datos = []
    for att in atributos:
        datos.append(input(f"Inserte {att}: "))
    instancias[i] = Automovil(*datos)

# Mostrar los datos
print("\nImprimiendo por pantalla los Vehículos:\n")
for n,veh in instancias.items():
    print(f"Datos del automóvil {n}:", veh)