from collections import defaultdict
from product import Producto
from client import Cliente
from shopping_cart import Carrito
from bills import Facturas

clientes = []
productos = []
carrito = []
factura =[]

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
    total_pagar = 0  
    total_impuesto = 0  
    for producto, cantidad in carrito:
        precio = int(producto.precio) 
        print(f"Codigo: {producto.codigo} Nombre: {producto.nombre}, Precio: Q{precio}, Descripción: {producto.descripcion}, Cantidad: {cantidad}")
        total_pagar += precio * cantidad  
        total_impuesto = (total_pagar * 0.12)+total_pagar
    print("Total a Pagar:", total_pagar)
    print("Impuesto:", total_impuesto)
    factura.append(Facturas(cliente.nombre, cliente.correo, cliente.NIT, carrito, total_pagar, total_impuesto))

def realizar_compra():
    carrito = []  
    cliente = seleccionar_cliente()
    if cliente is not None:
        menu_compra_opcion = input("Seleccione una opción:\n1. Comprar\n2. Terminar Compra y facturar\n")
        while menu_compra_opcion != "2":
            print("-----Menú Compra-----")
            for i, producto in enumerate(productos):
                print(f"{i}. Codigo: {producto.codigo} Nombre: {producto.nombre}, Precio: Q{int(producto.precio)}, Descripción: {producto.descripcion}")
            codigo_producto = input("Ingrese el código del producto: ")
            if codigo_producto.isdigit() and int(codigo_producto) < len(productos):
                cantidad_compra = input("Ingrese la cantidad que desea comprar: ")
                carrito.append((productos[int(codigo_producto)], int(cantidad_compra)))  
                print("Producto agregado al carrito")
            else:
                print("Código de producto inválido. Por favor, ingrese un número válido.")
            menu_compra_opcion = input("Seleccione una opción:\n1. Comprar\n2. Terminar Compra y facturar\n")
        print("Compra finalizada, imprimiendo factura...")
        imprimir_factura(cliente, carrito) 

def generar_reporte_facturas():
    print("-----Reporte de Facturas-----")
    for f in factura:
        print(f"Cliente: {f.nombre}, NIT: {f.NIT}")
        print("Productos Comprados:")
        for producto, cantidad in f.carrito:
            precio = int(producto.precio)
            print(f"Codigo: {producto.codigo} Nombre: {producto.nombre}, Precio: Q{precio}, Descripción: {producto.descripcion}, Cantidad: {cantidad}")
        print("Total a Pagar:", f.total_pagar)
        print("Impuesto:", f.total_impuesto)
        print("-----------------------------")
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
        "4": generar_reporte_facturas,
        "5": datos_estudiante,
        "6": salir
    }

    while True:
        opcion = input("Seleccione una opción:\n1. Registrar Producto\n2. Registrar Cliente\n3. Realizar Compra\n4. Reporte de facturas\n5. Datos del Estudiante\n6. Salir\n")
        
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":    
    menu()
