from clases import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

def name_of_object(arg):
    # check __name__ attribute (functions)
    try:
        return arg.__name__
    except AttributeError:
        pass
    for name, value in globals().items():
        if value is arg and not name.startswith('_'):
            return name


def relacion_instancia(instancia, lista_clases):
     nom_instancia = name_of_object(instancia)
     for clase in lista_clases:
        print(f"{nom_instancia} es instancia con relación a {clase.__name__}:",isinstance(instancia,clase))


# main()

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","DobleViga", 21)

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)
print("\nString con método definido en clase Vehiculo")
print(motocicleta.get_str())

print("")

#Verificar la relación que existe de la instancia motocicleta con: Vehículo, Automóvil, Particular,
#Carga, Bicicleta y Motocicleta.
clases = [Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta]
relacion_instancia(motocicleta, clases)
print("")
relacion_instancia(particular, clases)
print("")
relacion_instancia(carga, clases)
print("")
relacion_instancia(bicicleta, clases)




