import math

def esSalir(value):
    if value.lower() in ["fin", "end", "exit","salir", "terminar"]:
        return True
    return False


def ingresar_calificaciones():
    calificaciones = []
    clases = []
    continue_input = None

    while True:
        try:
            nombreClase = input("Ingrese el nombre de la materia: ")
            if esSalir(nombreClase):
                break
            if not nombreClase:
                print("El nombre de la materia no puede estar vacío. Intente nuevamente.")
                continue
            
            calificacionString = input("Ingrese una calificación: ")
            if esSalir(calificacionString):
                break

            if not calificacionString or not calificacionString or calificacionString.strip() == "" or calificacionString.lower() == "nan":
                print("La calificación no puede estar vacía. Intente nuevamente.")
                continue

            calificacion = float(calificacionString)
            if  math.isnan(float(calificacion)):
                print("La calificación no puede estar vacía. Intente nuevamente.")
                continue


            if(float(calificacion) < 0 or float(calificacion) > 10):
                print("La calificación debe estar entre 0 y 10. Intente nuevamente.")
                continue

            clases.append(nombreClase)
            calificaciones.append(abs(float(calificacion)))

            while True:
                continue_input = input("¿Desea ingresar otra calificación? (s/n): ")
                if continue_input.lower() in ["s", "n"]:
                    break
                else:
                    print("Por favor, ingrese 's' para sí o 'n' para no.")

            if continue_input.lower() == 'n':
                break

        except ValueError:
            print("Por favor, ingrese una calificación válida.")

    return clases, calificaciones

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral=5):
    clasesAprobadas=[]
    clasesReprobadas=[]
    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            clasesAprobadas.append(i)
        else:
            clasesReprobadas.append(i)
    return clasesAprobadas, clasesReprobadas

def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
    indiceMinimo = calificaciones.index(min(calificaciones))
    indiceMaximo = calificaciones.index(max(calificaciones))
    return indiceMinimo, indiceMaximo

def main():
    clases, calificaciones = ingresar_calificaciones()
    if not clases:
        print("No se ingresaron materias. Saliendo del programa.")
        return
    promedio = calcular_promedio(calificaciones)
    clasesAprobadas, clasesReprobadas = determinar_estado(calificaciones)
    minCal, maxCal = encontrar_extremos(calificaciones)

    print("\nResultados:")
    print(f"\tMaterias ingresadas")
    for i in range(len(clases)):
        print(f"\t\t{clases[i]}: {float(calificaciones[i]):.2f}")
    print(f"\tPromedio: {promedio:.2f}")
    print(f"\tMaterias aprobadas:")
    for i in clasesAprobadas:
        print(f"\t\t{clases[i]}: {float(calificaciones[i]):.2f}")
    print(f"\tMaterias reprobadas:")
    for i in clasesReprobadas:
        print(f"\t\t{clases[i]}: {float(calificaciones[i]):.2f}")
    print(f"\tCalificación máxima: {clases[maxCal]} {float(calificaciones[maxCal]):.2f}")
    print(f"\tCalificación mínima: {clases[minCal]} {float(calificaciones[minCal]):.2f}")
    print("Gracias por usar la calculadora de promedios. ¡Hasta luego!")

if __name__ == "__main__":
    main()