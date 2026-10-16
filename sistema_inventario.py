import os
import subprocess

def clear_console():
    # Use 'cls' for Windows (nt), and 'clear' for Mac and Linux
    command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
    subprocess.run(command, check=False)



class Producto:
    def __init__(self, nombre, precio, cantidad=0):
        if not isinstance(nombre, str):
            raise ValueError("El nombre del producto debe ser una cadena de texto.")
        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")

        try:
            precio = float(precio)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número válido.") from None
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError):
            raise ValueError("La cantidad debe ser un número entero válido.") from None
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.nombre = nombre.strip()
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def actualizar_cantidad(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número no negativo.")
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        if not isinstance(precio, (int, float)) or isinstance(precio, bool) or precio < 0:
            raise ValueError("El precio debe ser un número no negativo.")
        self.precio = precio

    def calcular_valor_total(self):
        return self.cantidad * self.precio


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise ValueError("Debe proporcionar un objeto de tipo Producto.")
        if producto.nombre in self.productos:
            raise ValueError("El producto ya existe en el inventario.")

        self.productos[producto.nombre] = producto

    def buscar_producto(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre del producto debe ser una cadena de texto.")
        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")

        return self.productos.get(nombre.strip(), None)

    def calcular_valor_inventario(self):
        return sum(producto.calcular_valor_total() for producto in self.productos.values())

    def listar_productos(self):
        return list(self.productos.values())


def menuPrincipal():
    inventario = Inventario()
    while True:
        clear_console()
        print("\n=== Sistema de Inventario ===")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            productoNombre = input("Ingrese el nombre del producto: ")
            if not productoNombre or productoNombre.strip() == "":
                print("El nombre del producto no puede estar vacío. Intente nuevamente.")
                continue
            productoPrecio = input("Ingrese el precio del producto: ")
            try:
                productoPrecio = float(productoPrecio)
                if productoPrecio < 0:
                    print("El precio no puede ser negativo. Intente nuevamente.")
                    continue
            except ValueError:
                print("El precio debe ser un número válido. Intente nuevamente.")
                continue

            productoCantidad = input("Ingrese la cantidad del producto: ")
            try:
                productoCantidad = int(productoCantidad)
                if productoCantidad < 0:
                    print("La cantidad no puede ser negativa. Intente nuevamente.")
                    continue
            except ValueError:
                print("La cantidad debe ser un número entero válido. Intente nuevamente.")
                continue

            try:
                producto = Producto(productoNombre, productoPrecio, productoCantidad)
                inventario.agregar_producto(producto)
                print(f"Producto '{productoNombre}' agregado exitosamente.")
            except (TypeError, ValueError) as e:
                print(f"Error al agregar el producto: {e}")

            input("Presione Enter para continuar...")

        elif opcion == "2":
            productoNombre = input("Ingrese el nombre del producto a buscar: ")
            try:
                producto = inventario.buscar_producto(productoNombre)
                if producto is None:
                    print(f"Producto '{productoNombre}' no encontrado en el inventario.")
                else:
                    print(f"Producto encontrado: {producto}")
            except (TypeError, ValueError) as e:
                print(f"Error al buscar el producto: {e}")
            input("Presione Enter para continuar...")
        elif opcion == "3":
            if not inventario.productos:
                print("No hay productos en el inventario.")
            for producto in inventario.listar_productos():
                print(producto)
            input("Presione Enter para continuar...")
        elif opcion == "4":
            if not inventario.productos:
                print("No hay productos en el inventario.")
            else:
                print(f"Valor total del inventario: ${inventario.calcular_valor_inventario():.2f}")
            input("Presione Enter para continuar...")
        elif opcion == "5":
            print("Saliendo del sistema de inventario.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            print("Presione Enter para continuar...\n")


if __name__ == "__main__":
    menuPrincipal()
