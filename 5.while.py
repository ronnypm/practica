# Asistente de programación

# Mostrar razonamiento
# ¡Tienes toda la razón! Se nos estaba quedando en el tintero el bucle while. Es fundamental y tiene un propósito muy diferente al del bucle for. Vamos a verlo ahora mismo.

# El Bucle while: Repetir Mientras Sea Verdad
# Un bucle while ejecuta un bloque de código una y otra vez, mientras una condición específica sea verdadera. En el momento en que la condición se vuelve falsa, el bucle se detiene.

# for vs. while: ¿Cuándo Usar Cada Uno?
# Esta es la diferencia clave que debes recordar:

# Bucle for: Lo usas cuando sabes cuántas veces quieres que se repita el bucle. Es un bucle de iteración definida.

# "Para cada producto en mi lista de inventario..." (Sabes que se repetirá 3 veces).

# "Para cada número en el rango del 1 al 10..." (Sabes que se repetirá 10 veces).

# Bucle while: Lo usas cuando no sabes cuántas veces se va a repetir, pero sí conoces la condición que debe cumplirse para continuar. Es un bucle de iteración indefinida.

# "Mientras el jugador tenga vidas..."

# "Mientras el usuario no escriba 'salir'..."

# "Mientras el stock sea mayor a 0..."

# ¡Cuidado con los Bucles Infinitos! ⚠️
# El error más común con un bucle while es crear un bucle infinito. Esto ocurre si la condición del while nunca se vuelve falsa. El programa se quedará atascado en el bucle para siempre.

# Python

# # # ¡PELIGRO! BUCLE INFINITO
# # x = 5
# # while x > 0:
# #     print("x sigue siendo mayor a 0")
# # # En este caso, el valor de x nunca cambia, por lo que la condición x > 0 siempre será verdadera.

# # CORRECTO
# x = 5
# while x > 0:
#     print(f"Cuenta regresiva: {x}")
#     x -= 1 # <-- Esta línea es crucial. Eventualmente hará que la condición sea falsa.
# print("¡Despegue!")


# Ejercicio Práctico: Simulación de Agotamiento de Stock
# Vamos a simular la venta de un solo producto hasta que se agote. Este es un caso de uso perfecto para un while, porque no sabemos exactamente cuántas ventas se necesitarán para acabar el stock.

# Tarea 1 (Preparación):

# *Importa el módulo random al inicio de tu script: import random. Lo usaremos para simular ventas de cantidades variables.

# *Crea una variable stock_naranjas y asígnale un valor inicial de 35.

# *Crea un contador ventas_hechas y ponlo en 0.

# Tarea 2 (El Bucle while):

# *Escribe un bucle while que se ejecute mientras stock_naranjas sea mayor que 0.

# Tarea 3 (Dentro del Bucle):

# *En cada vuelta del bucle, simula una venta. Crea una variable cantidad_vendida que sea un número aleatorio entre 1 y 5. Puedes usar random.randint(1, 5).

# *Importante: Asegúrate de que no vendes más de lo que tienes. Si el stock_naranjas es 3 y la cantidad_vendida aleatoria es 5, solo deberías vender 3. Un simple if puede arreglar esto, o puedes usar la función min(cantidad_aleatoria, stock_actual).

# *Resta la cantidad_vendida del stock_naranjas.

# *Incrementa en 1 el contador ventas_hechas.

# *Imprime un mensaje que informe de la venta, por ejemplo: Venta #1: Se vendieron 4 naranjas. Quedan 31.

# Tarea 4 (Después del Bucle):

# *Una vez que el bucle termine (porque el stock llegó a 0), imprime un mensaje final, como: "¡Stock de naranjas agotado! Se realizaron un total de 8 ventas."


# import random


# def poco_stock():
#     ventas_hechas = 0
#     stock_naranjas = 35
#     while stock_naranjas > 0:

#         cantidad_aleatoria = random.randint(1, 20)

#         cantidad_vendida = min(cantidad_aleatoria,stock_naranjas)

#         stock_naranjas -= cantidad_vendida
#         ventas_hechas += 1

#         print(f'Se vendieron {cantidad_vendida} naranjas, quedan {stock_naranjas}')
#     print(ventas_hechas)

# poco_stock()


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
imprimir_recivo(carrito)
