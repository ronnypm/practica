# Tarea 1 (con if/elif/else): Escribe una función analizar_precio(producto) que reciba un diccionario de producto y devuelva un string con una recomendación:

# Si el precio es menor a 1.00, debe devolver "Oferta!".

# Si el precio está entre 1.00 y 1.30 (incluido), debe devolver "Precio razonable".

# Si el precio es mayor a 1.30, debe devolver "Inversión premium".

# Tarea 2 (con Operador Ternario): Escribe una función es_popular(producto) que reciba un diccionario de producto. Usando un operador ternario, la función debe devolver "Popular" si el stock es mayor a 35, y "Normal" en caso contrario.

# Tarea 3 (Juntando Todo): Escribe un bucle for que recorra el inventario. En cada vuelta, llama a las dos funciones que creaste (analizar_precio y es_popular) e imprime un resumen para cada producto, así:


inventario = [
    {'nombre': 'manzanas', 'stock': 50, 'precio': 1.50},
    {'nombre': 'naranjas', 'stock': 35, 'precio': 0.90},
    {'nombre': 'platanos', 'stock': 40, 'precio': 1.20},
]


def analizar_precio(producto):
    precio = producto['precio']

    if precio < 1.00:
        return "Oferta!"
    elif precio <= 1.30:
        return 'Precio razonable'
    else:
        return "Inversión premium"


def es_popular(producto):
    return "Popular" if producto['stock'] > 35 else "Normal"


for p in inventario:
    print(f"{p['nombre']}: {analizar_precio(p)} ({es_popular(p)})")
