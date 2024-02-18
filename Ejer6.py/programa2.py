def ingresar_calificaciones():
    while True:
        try:
           r_str = input("Ingrese las notas por comas: ")
           calificaciones_lista = r_str.split(',')
           calificaciones_enteros = [int(calificacion) for calificacion in calificaciones_lista]
           return calificaciones_enteros
        except ValueError:
            print("Error: Formato no valido.")

def main():
    calificaciones_enteros = ingresar_calificaciones()
    print("Calificaciones como enteros:", calificaciones_enteros)

if __name__ == "__main__":
    main()