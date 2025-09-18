# class Producto:
#     def __init__(self, nombre_producto, precio_producto, stock_inicial):
#         # print(f"Creando el producto '{nombre_producto}'")

#         self.nombre = nombre_producto
#         self.precio = precio_producto
#         self.stock = stock_inicial


# productos = [Producto(nombre_producto="Manzana Fuji",
#                       precio_producto=1.50, stock_inicial=100),
#              Producto(nombre_producto="Naranja de Mesa",
#                       precio_producto=0.90, stock_inicial=150)
#              ]


# for p in productos:
#     print(f"{p.nombre} cuesta S/ {p.precio} y tiene un stock {p.stock}")


# class Usuario:
#     def __init__(self, nombre, email):
#         self.nombre = nombre
#         self.email = email
#         self.estado = False

#     def estado_usuario(self):
#         return 'Activo' if self.estado == True else "Inactivo"

#     def __str__(self):
#         return f"Nombre: {self.nombre}\nEmail: {self.email}\nEstado: {self.estado_usuario()}"


# usuario_1 = Usuario("Ronny", 'Ronny_pm@hotmail.com')
# print(usuario_1)


# ------------------------------------------------------------------------------


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self._stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if stock < 0:
            print("Stock no disponible")
        else:
            self._stock = stock

    def vender(self, cantidad):
        if self.stock < cantidad:
            print(f"Stock insuficiente, solo hay {self.stock}")
            return False
        else:
            self.stock -= cantidad
            print(f"Venta ralizada de {self.nombre} cantidad: {cantidad}")
            return True

    def reponer(self, cantidad):
        self.stock += cantidad


manzana = Producto("manzanas", 2, 20)
manzana.vender(21)
print(f"stock actual {manzana.stock} {manzana.nombre}")

manzana.reponer(10)
print(f"Stock final: {manzana.stock}")

print("\nIntentando asignar un stock negativo...")
manzana.stock = -50
print(f"Stock después de intentar asignar -50: {manzana.stock}")