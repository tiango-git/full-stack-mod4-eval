from clases import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

# Nombre del archivo donde se guardarán los datos
nom_archivo = "vehiculos.csv"

def name_of_object(arg):
    # check __name__ attribute (functions)
    try:
        return arg.__name__
    except AttributeError:
        pass
    for name, value in globals().items():
        if value is arg and not name.startswith('_'):
            return name



# Crear instancias
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","DobleViga", 21)
automovil = Automovil("Ferrari", "Enzo", 2, "355", "500")
particular2 = Particular("Suzuki", "Swift", 4, "180", "1200", 5)


# Guardar instancias en archivo
particular.guardar_datos_csv(nom_archivo)
carga.guardar_datos_csv(nom_archivo)
bicicleta.guardar_datos_csv(nom_archivo)
motocicleta.guardar_datos_csv(nom_archivo)


print("\n" + "#"*80 + "\n")


# Obtener todas las instancias creadas en base a la clase Vehiculo
# y guardarlas en el archivo
# Hacemos una copia de globals, porque sus datos varían durante el ciclo for
gl = globals().copy()
for name, value in gl.items():
    if isinstance(value, Vehiculo):
        print(f"Guardando instancia {name}")
        value.guardar_datos_csv(nom_archivo)


print("\n" + "#"*80 + "\n")


#Leer los datos según las instancias
instancias = [particular, carga, bicicleta, bicicleta]
for instancia in instancias:
    instancia.leer_datos_csv(nom_archivo)
    print("")


print("\n" + "#"*80 + "\n")


# Leer los datos según la clase
# Notar que si es una clase  y no una instancia, "leer_datos_csv" me pide 2 argumentos (self, nom_archivo)
# leer_datos_csv se modificó para que acepte una clase o una instancia
clases = [Automovil, Particular, Carga, Bicicleta, Motocicleta]
for clase in clases:
    clase.leer_datos_csv(clase,nom_archivo)
    print("")


