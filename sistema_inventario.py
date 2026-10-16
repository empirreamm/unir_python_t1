import os
def clear_console():
    # Use 'cls' for Windows (nt), and 'clear' for Mac and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

class Producto:
        
    def __init__(self, nombre, precio, cantidad=0):
        if not nombre or nombre.strip() == "" or nombre is None:
            raise ValueError("El nombre del producto no puede estar vacío.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        try:
            self.precio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser un número válido.")

        try:
            self.cantidad = int(cantidad)
        except ValueError:
            raise ValueError("La cantidad debe ser un número entero válido.")

        self.nombre = nombre.strip() if nombre else None

    def __str__(self):
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def actualizar_cantidad(self, cantidad):
        if cantidad < 0 or not isinstance(cantidad, (int, float)):
            raise ValueError("La cantidad debe ser un número entero no negativo.")
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        if precio < 0 or not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser un número no negativo.")
        self.precio = precio

    def calcular_valor_total(self):
        return self.cantidad * self.precio

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.nombre in self.productos:
            raise ValueError("El producto ya existe en el inventario.")

        if not isinstance(producto, Producto):
            raise ValueError("Debe proporcionar un objeto de tipo Producto.")
        
        self.productos[producto.nombre] = producto

    def buscar_producto(self, nombre):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not isinstance(nombre, str):
            raise ValueError("El nombre del producto debe ser una cadena de texto.")
        return self.productos.get(nombre, None)

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
            except ValueError as e:
                print(f"Error al agregar el producto: {e}")

            input("Presione Enter para continuar...")

        elif opcion == "2":
            productoNombre = input("Ingrese el nombre del producto a buscar: ")
            if not productoNombre or productoNombre.strip() == "":
                print("El nombre del producto no puede estar vacío. Intente nuevamente.")
                continue
            producto = inventario.buscar_producto(productoNombre)
            if producto:
                print(f"Producto encontrado: {producto}")
            else:
                print(f"Producto '{productoNombre}' no encontrado en el inventario.")
            input("Presione Enter para continuar...")
        elif opcion == "3":
            for producto in inventario.listar_productos():
                print(producto)
            input("Presione Enter para continuar...")
        elif opcion == "4":
            print(f"Valor total del inventario: ${inventario.calcular_valor_inventario():.2f}")
            input("Presione Enter para continuar...")
        elif opcion == "5":
            print("Saliendo del sistema de inventario.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            print("Presione Enter para continuar...")


if __name__ == "__main__":
    menuPrincipal()