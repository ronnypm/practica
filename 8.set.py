inventario = [
    {'nombre': 'manzanas', 'stock': 50, 'precio': 1.50},
    {'nombre': 'naranjas', 'stock': 35, 'precio': 0.90},
    {'nombre': 'platanos', 'stock': 40, 'precio': 1.20}
]


carrito = []


def buscar_producto(nombre_producto: str, inventario_lista: list) -> dict | None:
    for producto in inventario_lista:
        if nombre_producto == producto['nombre']:
            return producto
    return None


def imprimir_recivo(carrito_a_imprimir):
    total_final = 0
    print("---RECIVO DE VENTA---")
    for producto_dict, cantidad in carrito_a_imprimir:
        sub_total = producto_dict['precio'] * cantidad
        total_final += sub_total
        print(
            f"- {cantidad} {producto_dict['nombre']} (@ S/ {producto_dict['precio']} c/u) - Subtotal: S/ {sub_total}")
    print('-' * 20)
    print(f'TOTAL A PAGAR S/ {round(total_final, 2)}')


try:
    while True:

        nombre_producto = input(
            "Ingrese el nombre del producto deseado: ").lower().strip()

        if not nombre_producto:
            print('Error: No ingreso ningun nombre de producto! ')
            continue
        if nombre_producto == 'terminar':
            break

        producto_encontrado = buscar_producto(nombre_producto, inventario)

        if producto_encontrado is None:
            print("Error: Producto no existe.")
            continue

        while True:
            try:
                producto_cantidad = input(
                    f'Ingrese la cantidad que desee de {nombre_producto}(1-9): ')

                if not producto_cantidad:
                    print('Error: Ingrese una cantidad!')
                    continue
                producto_cantidad_int = int(producto_cantidad)
                if producto_cantidad_int > producto_encontrado['stock']:
                    print(
                        f"Error: Stock insuficiente. Solo quedan {producto_encontrado['stock']} {producto_encontrado['nombre']}.")
                    continue
                break

            except ValueError:
                print('Ingrese un numero porfavor')

        producto_encontrado['stock'] -= producto_cantidad_int
        carrito.append((producto_encontrado, producto_cantidad_int))
        print("Producto anadido")
except KeyboardInterrupt:
    print("\nEl usuario decidio terminar con el programa.")


nombre_productos_comprados = [descripcion['nombre']
                              for descripcion, cant in carrito]
print(nombre_productos_comprados)


set_productos = set(nombre_productos_comprados)
print(set_productos)
# imprimir_recivo(carrito)s
