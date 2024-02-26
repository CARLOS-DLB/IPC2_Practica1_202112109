from product import Producto
from client import Cliente
from shopping_cart import Carrito

clientes = []
productos = []
carrito = []

def registrar_producto():
    opcion_registro_producto = input("Seleccione una opción:\n1. Registrar Producto\n2. Salir\n")
    while opcion_registro_producto != "2":
        codigo_producto = input("Ingrese el código del producto: ")
        nombre_producto = input("Ingrese el nombre del producto: ") 
        descripcion_producto = input("Ingrese la descripción del producto: ")   
        precio_producto = input("Ingrese el precio del producto: Q")       
        producto = Producto(codigo_producto, nombre_producto, descripcion_producto, precio_producto)
        productos.append(producto) 
        print("Producto registrado exitosamente")
        opcion_registro_producto = input("Seleccione una opción:\n1. Registrar Producto\n2. Salir\n")
    print("Saliendo del registro de productos")
def registrar_cliente():
    opcion_registro_cliente = input("Seleccione una opción:\n1. Registrar Cliente\n2. Salir\n")
    while opcion_registro_cliente != "2":
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        correo_cliente = input("Ingrese el correo electrónico del cliente: ")
        nit_cliente = input("Ingrese el NIT del cliente: ")
        cliente = Cliente(nombre_cliente, correo_cliente, nit_cliente)
        clientes.append(cliente)
        print("Cliente registrado exitosamente")
        opcion_registro_cliente = input("Seleccione una opción:\n1. Registrar Cliente\n2. Salir\n")
    print("Saliendo del registro de clientes")
def seleccionar_cliente():
    print("-----Clientes Registrados-----")
    for cliente in clientes:
        print(f"Nombre: {cliente.nombre}, Correo: {cliente.correo}, NIT: {cliente.NIT}")
    nit_cliente = input("Ingrese el NIT del cliente: ")
    for cliente in clientes:
        if cliente.NIT == nit_cliente:
            return cliente
    print("Cliente no encontrado. Por favor, ingrese un NIT válido.")
    return None
def imprimir_factura(cliente, carrito):
    print("-----Factura-----")
    print("Nombre del Cliente: ", cliente.nombre)
    print("NIT del Cliente: ", cliente.NIT)
    print("Correo del Cliente: ", cliente.correo)
    print("Productos Comprados:")
    total_pagar = 0  # Initialize total_pagar variable
    for producto, cantidad in carrito:
        precio = int(producto.precio)  # Convert precio to integer
        print(f"Codigo: {producto.codigo} Nombre: {producto.nombre}, Precio: Q{precio}, Descripción: {producto.descripcion}, Cantidad: {cantidad}")
        total_pagar += precio * cantidad  # Calculate total price
    print("Total a Pagar:", total_pagar)

def realizar_compra():
    cliente = seleccionar_cliente()
    if cliente is not None:
        carrito = []
        menu_compra_opcion = input("Seleccione una opción:\n1. Comprar\n2. Terminar Compra y facturar\n")
        while menu_compra_opcion != "2":
            print("-----Menú Compra-----")
            for producto in productos:
                print(f"Codigo: {producto.codigo} Nombre: {producto.nombre}, Precio: Q{int(producto.precio)}, Descripción: {producto.descripcion}")
            codigo_producto = input("Ingrese el código del producto: ")
            cantidad_compra = input("Ingrese la cantidad que desea comprar: ")
            carrito.append((productos[int(codigo_producto)], int(cantidad_compra)))
            print("Producto agregado al carrito")
            menu_compra_opcion = input("Seleccione una opción:\n1. Comprar\n2. Terminar Compra y facturar\n")
        print("Compra finalizada, imprimiendo factura...")
        imprimir_factura(cliente, carrito)
def reporte_compra():
    print("-----Reporte de Compras-----")
    print("Nombre del Cliente: ")
    print("NIT del Cliente: ")
    print("Correo del Cliente: ")
    print("Productos Comprados: ")
    print("Total a Pagar: ")

def datos_estudiante():
    print("Nombre: Carlos David De León Barrios")
    print("Carné: 202112109")
    print("Curso: IPC2")

def salir():
    print("Saliendo del programa.")
    exit()

def menu():
    opciones = {
        "1": registrar_producto,
        "2": registrar_cliente,
        "3": realizar_compra,
        "4": reporte_compra,
        "5": datos_estudiante,
        "6": salir
    }

    while True:
        opcion = input("Seleccione una opción:\n1. Registrar Producto\n2. Registrar Cliente\n3. Realizar Compra\n4. Reporte de Compra\n5. Datos del Estudiante\n6. Salir\n")
        
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":    
    menu()

