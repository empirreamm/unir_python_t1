def isExit(value):
    if value.lower() in ["fin", "end", "exit"]:
        return True
    return False

def ingresar_calificaciones():
    calificaciones = []
    classes = []

    while True:
        try:
            className = input("Ingrese el nombre de la materia: ")
            if isExit(className):
                break
            if not className:
                print("El nombre de la materia no puede estar vacío. Intente nuevamente.")
                continue
            
            calificacion = input("Ingrese una calificación: ")
            if isExit(calificacion):
                break

            if not calificacion:
                print("La calificación no puede estar vacía. Intente nuevamente.")
                continue

            if(float(calificacion) < 0 or float(calificacion) > 10):
                print("La calificación debe estar entre 0 y 10. Intente nuevamente.")
                continue

            classes.append(className)
            calificaciones.append(abs(float(calificacion)))

            continue_input = input("¿Desea ingresar otra calificación? (s/n): ")
            if continue_input.lower() != 'n':
                continue
            break
        except ValueError:
            print("Por favor, ingrese una calificación válida.")

    return classes, calificaciones

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral=5):
    passedClasses=[]
    failedClasses=[]
    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            passedClasses.append(i)
        else:
            failedClasses.append(i)
    return passedClasses, failedClasses

def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
    return min(calificaciones), max(calificaciones)

def main():
    classes, calificaciones = ingresar_calificaciones()
    promedio = calcular_promedio(calificaciones)
    passedClasses, failedClasses = determinar_estado(calificaciones)
    minCal, maxCal = encontrar_extremos(calificaciones)

    print("\nResultados:")
    print(f"\tMaterias ingresadas")
    for i in range(len(classes)):
        print(f"\t\t{classes[i]}: {float(calificaciones[i]):.2f}")
    print(f"\tPromedio: {promedio:.2f}")
    print(f"\tMaterias aprobadas:")
    for i in passedClasses:
        print(f"\t\t{classes[i]}: {float(calificaciones[i]):.2f}")
    print(f"\tMaterias reprobadas:")
    for i in failedClasses:
        print(f"\t\t{classes[i]}: {float(calificaciones[i]):.2f}")
    print(f"\tCalificación máxima: {maxCal:.2f}")
    print(f"\tCalificación mínima: {minCal:.2f}")
    print("Gracias por usar la calculadora de promedios. ¡Hasta luego!")

if __name__ == "__main__":
    main()