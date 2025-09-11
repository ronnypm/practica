# Un diccionario simple representando un usuario
# usuario = {
#     "id_usuario": 101,
#     "nombre": "Elena",
#     "activa": True,
#     "permisos": ["lectura", "escritura"]
# }

# # Acceder a un valor por su clave
# print(usuario["nombre"])  # Salida: Elena

# # Añadir o modificar un par clave-valor
# usuario["email"] = "elena@correo.com"  # Añade una nueva clave
# usuario["activa"] = False             # Modifica una clave existente

# # Forma segura de acceder a una clave (evita errores si no existe)
# # .get() devuelve None si la clave no se encuentra, en lugar de un error.
# telefono = usuario.get("telefono")
# print(telefono) # Salida: None

# # Iterar sobre un diccionario (la forma más común y útil)
# print("\n--- Datos del Usuario ---")
# for clave, valor in usuario.items():
#     print(f"{clave.capitalize()}: {valor}")


# . Ejercicio Práctico: Mini-proyecto de Inventario
# Imagina que estás creando un sistema simple para gestionar el inventario de una frutería. Necesitas llevar la cuenta de cuántas unidades tienes de cada producto.

# Tu Misión:

# 1 Crea un diccionario llamado inventario que represente el stock inicial de la tienda. Usa los nombres de las frutas como claves (strings) y la cantidad en stock como valores (enteros).

# *'manzanas': 50

# *'naranjas': 35

# *'platanos': 40

# 2 Escribe una función llamada procesar_venta que reciba tres argumentos: el diccionario inventario, el producto vendido (string) y la cantidad_vendida (entero).

# 3 La lógica dentro de la función debe ser la siguiente:

# * Primero, verifica si el producto que se quiere vender existe como clave en el inventario.

# * Si existe, comprueba si la cantidad_vendida es menor o igual al stock disponible.

#       *Si hay stock suficiente, resta la cantidad vendida del inventario y muestra un mensaje como: "Venta exitosa. Quedan 45 manzanas."

#       *Si no hay stock suficiente, muestra un mensaje como: "Stock insuficiente. Solo quedan 35 naranjas."

#       *Si el producto no existe en el inventario, muestra un mensaje como: "Lo sentimos, el producto 'fresas' no está en el inventario."

# 4 La función no necesita devolver nada, solo debe modificar el diccionario que recibe y mostrar los mensajes.

# 5 Al final de tu script, llama a la función procesar_venta varias veces para probar todos los casos:

#   *Una venta exitosa ('manzanas', 5).

#   *Un intento de venta con stock insuficiente ('naranjas', 50).

#   *Un intento de venta de un producto que no existe ('fresas', 10).

#   *Finalmente, imprime el diccionario inventario completo para ver el estado final después de las ventas.


# inventario = {
#     'manzanas': 50,
#     'naranjas': 35,
#     'platanos': 40,
# }

# def procesar_venta(inventario:dict, producto:str, cantidad_vendida:int):

#     if producto not in inventario:
#         return f"Lo sentimos, el producto {producto} no está en el inventario."

#     if cantidad_vendida <= inventario[producto]:
#         inventario[producto] -= cantidad_vendida
#         return f"Venta exitosa. Quedan {inventario.get(producto)} {producto}."
#     return f"Stock insuficiente. Solo quedan {inventario.get(producto)} {producto}"


# print(procesar_venta(inventario,'manzanas',5))
# print(procesar_venta(inventario,'naranjas',50))
# print(procesar_venta(inventario,'fresas',10))
# print(inventario)


# ----------------------------------------------------------------


inventario = [
    {'nombre': 'manzanas', 'stock': 50, 'precio': 1.50},
    {'nombre': 'naranjas', 'stock': 35, 'precio': 0.90},
    {'nombre': 'platanos', 'stock': 40, 'precio': 1.20}
]

carrito = {
    'manzanas': 3,
    'platanos': 5,
    'naranjas': 2,
}

def buscar_producto(nombre_producto, inventario):

    for producto in inventario:
        if nombre_producto == producto["nombre"]:
          return producto
    return None
    

def procesar_venta(inventario: dict, producto: str, cantidad_vendida: int):
    producto_encontrado = buscar_producto(producto,inventario)
    if producto_encontrado is None:
        return f"Lo sentimos, el producto {producto} no está en el inventario."
        
    if producto_encontrado:
        if cantidad_vendida <= producto_encontrado['stock']:
            producto_encontrado['stock'] -= cantidad_vendida
            return f"Venta exitosa. Quedan {producto_encontrado["stock"]} {producto_encontrado['nombre']}."
        return f"Stock insuficiente. Solo quedan {producto_encontrado["stock"]} {producto_encontrado["nombre"]}"


def procesar_carrito(inventario: dict, carrito: dict):

    for producto, cantidad in carrito.items():
        print(f"Producto {producto}, Cantidad: {cantidad}")
        resultado = procesar_venta(inventario, producto, cantidad)
        print(resultado)


print("--- Iniciando Ventas ---")
print(procesar_venta(inventario, 'manzanas', 10))
print(procesar_venta(inventario, 'platanos', 50)) # Stock insuficiente
print(procesar_venta(inventario, 'fresas', 5))   # Producto no existe
print(procesar_venta(inventario, 'naranjas', 5))
print("\n--- Inventario Final ---")
print(inventario)      


