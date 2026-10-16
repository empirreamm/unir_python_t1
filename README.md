# Calculadora de promedios

Programa de consola escrito en Python para registrar materias y sus calificaciones, calcular el promedio y mostrar cuáles están aprobadas o reprobadas.

## Requisitos

- Python 3.6 o posterior
- No requiere dependencias externas

## Uso

Desde la carpeta del proyecto, ejecuta:

```bash
python calculadora_promedios.py
```

En algunos sistemas puede ser necesario usar `python3`:

```bash
python3 calculadora_promedios.py
```

Ingresa el nombre de una materia y una calificación entre `0` y `10`. Después podrás indicar si deseas añadir otra calificación (`s` para continuar o `n` para terminar). También puedes escribir `fin`, `end` o `exit` —sin importar mayúsculas o minúsculas— en cualquiera de las entradas para dejar de ingresar datos.

## Resultados

Al terminar, el programa muestra las materias y sus calificaciones, el promedio, las materias aprobadas (calificación igual o superior a `5`), las reprobadas y las calificaciones máxima y mínima.

## Ejemplo

```text
Ingrese el nombre de la materia: Matemáticas
Ingrese una calificación: 8
¿Desea ingresar otra calificación? (s/n): s
Ingrese el nombre de la materia: Historia
Ingrese una calificación: 4
¿Desea ingresar otra calificación? (s/n): n

Resultados:
    Materias ingresadas
        Matemáticas: 8.00
        Historia: 4.00
    Promedio: 6.00
    Materias aprobadas:
        Matemáticas: 8.00
    Materias reprobadas:
        Historia: 4.00
    Calificación máxima: 8.00
    Calificación mínima: 4.00
```
