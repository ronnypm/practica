# # Creando una lista de nombres de usuario para un sistema
# usuarios = ["Carlos", "Ana", "Luis", "Marta"]

# # Accediendo al primer elemento de la lista (índice 0)
# primer_usuario = usuarios[0]  
# print(f"El primer usuario es: {primer_usuario}")

# # Accediendo al último elemento (índice -1)
# ultimo_usuario = usuarios[-1]
# print(f"El último usuario es: {ultimo_usuario}")

# Ejercicio 1

# 1.Crea una lista llamada inventario con al menos cinco productos (cadenas de texto).

# 2.Imprime el tercer producto de la lista (recuerda que los índices empiezan en 0).

# 3.Imprime el último producto de la lista usando un índice negativo.

# list_product = ["Manzana", "Pera", "Arroz", "Silla", "Meza"]

# third_product = list_product[2]
# last_product = list_product[-1]

# print(f'Tercer Producto: {third_product}\nUltimo Producto: {last_product}')


# ---------------------------------------------------------------------------------------





# EJERCICIO 2


# *.append(): Agrega un elemento al final de la lista.

# *.insert(): Inserta un elemento en una posición específica.

# *.remove(): Elimina un elemento por su valor.

# *.pop(): Elimina un elemento por su índice y lo devuelve.

# Tu Siguiente Reto
# Usando la misma lista list_product que creaste, realiza las siguientes operaciones, imprimiendo el estado de la lista después de cada paso para ver los cambios:

# 1. Agrega un nuevo producto a la lista (usando .append()).

# 2. Inserta un producto en la segunda posición (índice 1).

# 3. Elimina el producto llamado "Arroz".

# 4. Elimina el último producto de la lista y guarda ese producto en una nueva variable.


# list_product = ["Manzana", "Pera", "Arroz", "Silla", "Meza"]
# print(f'Lista original: "{list_product}"\n')
# list_product.append("Computadora")
# print(f'Lista con "appent": {list_product}\n')
# list_product.insert(1,"Laptop")
# print(f'Lista con "insert": {list_product}\n')
# list_product.remove("Arroz")
# print(f'Lista con "remove": {list_product}\n')
# pop_product = list_product.pop()
# print(f'Listsa con "pop": {list_product}')




# ------------------------------------------------------------------------






# EJERCICIO 3


# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Ejemplo 1: Tomar los primeros 4 elementos (desde el índice 0 hasta el 4, sin incluirlo)
# primeros_cuatro = numeros[0:4]  
# print(f'Los primeros 4 números son: {primeros_cuatro}') 
# # Resultado: [0, 1, 2, 3]

# # Ejemplo 2: Tomar del índice 3 al 7 (el 7 no se incluye)
# pedazo_medio = numeros[3:7]     
# print(f'Un pedazo del medio es: {pedazo_medio}') 
# # Resultado: [3, 4, 5, 6]

# # Ejemplo 3: Un atajo. Si dejas el inicio vacío, Python asume que es 0.
# pedazo_con_atajo = numeros[:5]  
# print(f'Un pedazo con atajo es: {pedazo_con_atajo}')
# # Resultado: [0, 1, 2, 3, 4]

# # Ejemplo 4: Otro atajo. Si dejas el fin vacío, Python asume que es el final de la lista.
# hasta_el_final = numeros[6:]    
# print(f'Del sexto elemento hasta el final: {hasta_el_final}')
# # Resultado: [6, 7, 8, 9]

# # Ejemplo 5: Usando el 'paso' para saltar elementos.
# impares = numeros[1::2]         
# print(f'Solo los números impares: {impares}')
# # Resultado: [1, 3, 5, 7, 9]




# ¡Perfecto! Continuemos.

# Aquí tienes el reto de slicing, para que apliques lo que vimos en los ejemplos.

# Tu reto:
# Usando tu lista list_product, realiza lo siguiente:

#1. Crea una nueva lista llamada primeros_tres que contenga solo los tres primeros productos.

#2. Crea otra lista llamada segundos_a_penultimo que contenga los productos desde el segundo hasta el penúltimo.

# #3. Crea una última lista llamada invertida que contenga todos los productos pero en orden inverso (sin usar el método .reverse()).




# list_product = ["Manzana", "Pera", "Arroz", "Silla", "Meza"]

# first_three_products = list_product[:3]
# middle_products = list_product[1:-1]
# reversed_products = list_product[::-1]

# print(f'Primero tres productos: {first_three_products}')
# print(f'Segunod a penultimo productos: {middle_products}')
# print(f'Lista inversa: {reversed_products}')



# ---------------------------------------------------------------------------------


# # Creación de una lista de tareas (to-do list)
# tareas = ["Hacer la compra", "Llamar al cliente", "Preparar la presentación"]
# print(f"Mi lista de tareas inicial: {tareas}")

# # --- Acceder a elementos ---
# # Accedemos por su índice (el primero es 0)
# primera_tarea = tareas[0]
# print(f"Mi primera tarea es: '{primera_tarea}'")

# # Accedemos al último elemento con índice negativo
# ultima_tarea = tareas[-1]
# print(f"Mi última tarea es: '{ultima_tarea}'")

# # --- Modificar elementos ---
# # El cliente canceló, actualizamos la tarea
# tareas[1] = "Enviar correo de seguimiento"
# print(f"Lista actualizada: {tareas}")

# # --- Añadir elementos ---
# # Añadir una tarea al final
# tareas.append("Revisar el código del proyecto")
# print(f"Añadí una tarea al final: {tareas}")

# # Insertar una tarea en una posición específica
# tareas.insert(1, "Reunión de equipo a las 10am")
# print(f"Inserté una tarea importante al principio: {tareas}")

# # --- Eliminar elementos ---
# # Eliminar el último elemento y guardarlo
# tarea_completada = tareas.pop()
# print(f"Tarea completada: '{tarea_completada}'. Lista restante: {tareas}")

# # Eliminar un elemento por su índice
# del tareas[0]
# print(f"Eliminé la primera tarea: {tareas}")

# # Eliminar un elemento por su valor (la primera ocurrencia)
# tareas.remove("Enviar correo de seguimiento")
# print(f"Eliminé una tarea específica: {tareas}")



# precios = [120.50, 89.99, 34.75, 250.00]
# impuesto = 0.16 # 16% de impuesto


# for precio in precios:
#     precio_final = precio * (1 + impuesto)
#     print(f'Precio original: /s {precio}\nPrecio con impuesto: /s {precio_final:.2f}')




# ---------------------------------------------------------------------




# Ejercicio 1: Gestor de Inventario Simple

# Crea un programa que simule el inventario de una tienda.

# Crea una lista llamada inventario con 3 productos iniciales (como strings).

# Simula la llegada de un nuevo producto: pide al usuario que ingrese el nombre de un producto y añádelo al final de la lista.

# Simula una venta: pide al usuario el nombre del producto vendido y elimínalo de la lista. Si el producto no existe, muestra un mensaje de error.

# Al final, muestra el inventario actualizado.


# inventario = ['Camisa', 'Jean', 'Polo']
# print(f'Inventario inicial: {inventario}')

# nuevo_producto = input('Ingrese un nuevo producto: ').strip().title()

# if nuevo_producto:
#     inventario.append(nuevo_producto)
#     print(f'Exito! "{nuevo_producto}" fue agregado a la lista')
# else:
#     print('Error! No se ingreso eun nombre de producto valido.')

# producto_vendido = input('Que producto se vendio? : ').strip().title()


# if producto_vendido in inventario:
#     inventario.remove(producto_vendido)
#     print((f'Producto comprado fue eliminado del inventario:{producto_vendido}'))
# else:
#     print(f'El producto {producto_vendido} no se encuentra en la lista.')

# print('\n---Resumen Final---\n')
# print(f'Inventario final: {inventario}')


# -------------------------------------------------------------------------------------



# Ejercicio 2: Calificador de Notas 📝
# Crea una lista llamada notas con 5 calificaciones numéricas (pueden ser flotantes, como 8.5, o enteras, como 7).

#1. Calcula y muestra el promedio de las notas. (Pista: las funciones sum() y len() son tus amigas).

#2. Encuentra y muestra la nota más alta y la más baja. (Pista: max() y min() te ayudarán).

#3. "Ajuste de notas": Tienes que modificar la lista original. Suma 0.5 a cada nota, pero con una condición: ninguna nota puede superar el 10. Si al sumar 0.5 una nota pasa de 10, su valor final deberá ser 10.






# grades_list = [3, 7, 9.8, 5, 8]

# average_grade = sum(grades_list) / len(grades_list)

# highest_grade = max(grades_list)
# min_grade = min(grades_list)

# grades_to_update = [min(10,grade + 0.5) for grade in grades_list]

# passing_grades = [grade for grade in grades_to_update if grade >= 7]

# print(grades_list)
# print(average_grade)
# print(highest_grade)
# print(min_grade)
# print(grades_to_update)
# print(f'Notas mayor a 7: {passing_grades}')





# -------------------------------------------------------------------------




# Mini-Proyecto: Lista de Tareas (To-Do List) ✅
# Requisitos:

# Crea una lista vacía para almacenar las tareas.

# Crea un bucle infinito (while True) que muestre un menú de opciones al usuario:

# Agregar tarea

# Marcar tarea como completada (eliminarla)

# Mostrar todas las tareas

# Salir

# Agregar Tarea: Pide al usuario el nombre de la tarea y añádela a la lista.

# Marcar como Completada: Primero, muestra las tareas con su número de índice para que el usuario pueda elegir (ej: 1. Hacer la compra). Luego, pídele el número de la tarea que quiere completar y elimínala. Importante: Maneja el caso en que el usuario ingrese un número inválido (ej. un número que no corresponda a ninguna tarea o texto).

# Mostrar Tareas: Si la lista está vacía, muestra un mensaje amigable ("¡No hay tareas pendientes!"). Si no, muestra todas las tareas de forma ordenada.

# Salir: Termina el bucle y el programa.

lista_tareas  = ['comprar fruta', 'lavar los platos']


while True:
    lista_opciones = ['Agregar tarea',
                'Marcar tarea como completada',
                'Mostrar todas las tareas',    
                'Salir']
    
    for i, opcion_menu in enumerate(lista_opciones,1):
        print(f'{i}. {opcion_menu}')


    try:
        opcion_elegida = int(input('Ingrese una opcion: '))
    except ValueError:
        print('Error! Por favor ingrese solo un numero')
        continue

    if opcion_elegida == 1:
        nueva_tarea = input(f'Ingrese la nueva tares: ').strip()
        if nueva_tarea:
            lista_tareas.append(nueva_tarea)
            print(f'Tarea {nueva_tarea} agregada correctamente!')
        else:
            print('La tarea no puede estar vacia')

    elif opcion_elegida == 2:
        print('\n---Marcar como tarea completada---')
        if not lista_tareas:
            print('No hay tareas para completar.')
            continue

        for i, tarea in enumerate(lista_tareas,1):
            print(f'{i}. {tarea}')


        try:
            tarea_completada = int(input('Ingrese el numero de la tarea a completar: '))
            if 1 <=  tarea_completada <= len(lista_tareas):
                tarea_eliminada = lista_tareas.pop(tarea_completada - 1)
                print(f'Tarea {tarea_eliminada} completada.')
            else:
                print('Error! numero fuera de rango.')
        except ValueError:
            print('Error: Por favor, ingrese un numero valido.')

        
    elif opcion_elegida == 3:
        if not lista_tareas:
            print('Felecidades! No tiene tareas pendientes.')
        else: 
            for i, tarea in enumerate(lista_tareas,1):
                print(f'{i}. {tarea}')

            
    elif opcion_elegida == 4: 
        print('Hasta luego!')
        break
    else:
        print(f'Error: Opcion no valida. Por favor, elija del 1 al {len(lista_opciones)}')
        






    





  