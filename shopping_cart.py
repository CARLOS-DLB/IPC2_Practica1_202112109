class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def obtener_total(self):
        return sum([producto.precio for producto in self.productos])