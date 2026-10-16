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

# Sistema de inventario

Programa de consola para administrar productos, sus precios y las cantidades disponibles.

## Requisitos

- Python 3.6 o posterior
- No requiere dependencias externas

## Uso

Desde la carpeta del proyecto, ejecuta:

```bash
python sistema_inventario.py
```

En algunos sistemas puede ser necesario usar `python3`:

```bash
python3 sistema_inventario.py
```

## Opciones

El menú permite:

1. **Agregar producto:** ingresa el nombre, el precio y la cantidad. El nombre se guarda sin los espacios al principio y al final, conservando mayúsculas y minúsculas. No se permiten productos duplicados, precios negativos ni cantidades negativas.
2. **Buscar producto:** la búsqueda usa el nombre exacto, incluidas mayúsculas, minúsculas y espacios. Para encontrar un producto, escribe el nombre tal como quedó guardado (sin los espacios exteriores que se recortaron al agregarlo). Si no existe una coincidencia exacta, el programa muestra un aviso.
3. **Listar productos:** muestra los productos registrados.
4. **Calcular valor total del inventario:** suma el precio de cada producto multiplicado por su cantidad.
5. **Salir:** termina el programa.

Los precios deben ser números válidos y las cantidades deben ser enteros no negativos. El programa informa de los datos inválidos y permite volver al menú.
