class Producto:
    def __init__(self, nombre_producto, precio_producto, stock_inicial):
        # print(f"Creando el producto '{nombre_producto}'")

        self.nombre = nombre_producto
        self.precio = precio_producto
        self.stock = stock_inicial


productos = [Producto(nombre_producto="Manzana Fuji",
                      precio_producto=1.50, stock_inicial=100),
             Producto(nombre_producto="Naranja de Mesa",
                      precio_producto=0.90, stock_inicial=150)
             ]


for p in productos:
    print(f"{p.nombre} cuesta S/ {p.precio} y tiene un stock {p.stock}")
