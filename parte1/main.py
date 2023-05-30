from clases import Automovil


# Obtener datos, mostrando los textos del ejemplo
def obtener_datos():
    msg = [
            'Inserte la marca del automóvil: ',
            'Inserte el modelo: ',
            'Inserte el número de ruedas: ',
            'Inserte la velocidad en km/h: ',
            'Inserte el cilindraje en cc: '
            ]
    datos = []
    for m in msg:
        datos.append(input(m))
    return datos


# Mostrando los textos del ejemplo
def main():
    instancias = {}

    # Pedir los datos y guardarlos
    cantidad = int(input("Cuantos vehículos desea insertar: "))
    for i in range(1,cantidad+1):
        print(f"\nDatos del automóvil {i}")
        instancias[i] = Automovil(*obtener_datos())

    # Mostrar los datos
    print("\nImprimiendo por pantalla los Vehículos:\n")
    for n,veh in instancias.items():
        print(f"Datos del automóvil {n}:", veh)


# Versión genérica, independiente de los nombres de atributos y la cantidad de estos
def main2():
    instancias = {}
    atributos = list(Automovil.__init__.__code__.co_varnames)[1:]

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
        print(f"Datos del automóvil {n}:", veh.get_str())





if __name__ == "__main__":
    main()
    print("\n\nAhora, versión genérica (independiente de los atributos)\n")
    main2()
