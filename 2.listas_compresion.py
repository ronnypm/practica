# Una lista de comprensión es una forma elegante y concisa de crear listas. Piensa en ella como un atajo para un bucle for que construye una lista. En lugar de escribir varias líneas, lo resuelves todo en una sola.

# La sintaxis básica es:
# nueva_lista = [expresion for elemento in iterable if condicion]

# Vamos a desglosarlo:

# [expresion: Lo que quieres hacer con cada elemento (ej: elemento * 2, elemento['nombre']).

# for elemento in iterable: El bucle for normal que recorre una lista, tupla, etc.

# if condicion]: (Opcional) Un filtro para incluir solo los elementos que cumplan una condición.


inventario = [
    {'nombre': 'manzanas', 'stock': 50, 'precio': 1.50},
    {'nombre': 'naranjas', 'stock': 35, 'precio': 0.90},
    {'nombre': 'platanos', 'stock': 40, 'precio': 1.20}
]


def precios_productos():

    precios = [producto["precio"] for producto in inventario]
    return precios


def precio_mas_igv(precios):
    precio_final = [round(precio*1.18,2) for precio in precios]
    return precio_final


def stock(inventario):
    productos_poco_stock = [producto['nombre']
                            for producto in inventario if producto['stock'] <= 40]

    return productos_poco_stock


def informacion_del_inventario():
    precio_original = precios_productos()
    precion_final = precio_mas_igv(precio_original)
    poco_stock = stock(inventario)
    return (precio_original, precion_final, poco_stock)


datos = informacion_del_inventario()
precio, precio_igv, stock_bajo = datos


def datos_del_inventario(precio_bruto, precio_neto, stock):
    print(
        f'El precio individual de todos los productos son: {precio_bruto}\nPrecios mas IGV: {precio_neto}\nProductos con poco stock: {stock}')

datos_del_inventario(precio,precio_igv,stock_bajo)