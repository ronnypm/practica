# Ojo: la coma al final es OBLIGATORIA para que Python sepa que es una tupla.


# punto_3d = (10, 20, 5)

# # Acceder por índice
# eje_x = punto_3d[0]
# print(f"Coordenada X: {eje_x}")

# # Recorrer con un bucle
# print("Recorriendo la tupla:")
# for valor in punto_3d:
#     print(valor)

# # Comprobar si un elemento existe
# if 20 in punto_3d:
#     print("El valor 20 existe en la tupla.")



# El Poder del Desempaquetado (Tuple Unpacking)
# Una de las características más elegantes y útiles de las tuplas es el "desempaquetado". Te permite asignar los valores de una tupla a múltiples variables de una sola vez.

# coordenadas = (5,20)

# latitud,lon= coordenadas

# print(f'{lon}')

# También se pueden crear sin paréntesis (esto se llama "empaquetado de tuplas")
# otra_config = "smtp.server.com", 587


# Ejercicio
# Para afianzar esto, vamos a usar el desempaquetado.

# Crea una función llamada analizar_precios que reciba una lista de números (precios).

# Dentro de la función, encuentra el precio más alto y el más bajo de la lista (puedes usar max() y min()).

# La función debe retornar ambos valores. Por defecto, si retornas más de un valor, Python los empaqueta en una tupla.

# Fuera de la función, llama a analizar_precios con una lista de ejemplo y usa el desempaquetado para guardar el precio máximo y mínimo en dos variables separadas (precio_max y precio_min).

# Imprime las dos variables.






# def obtener_max_y_min(numeros):
#     return(max(numeros), min(numeros))

# precios = [12,656,78,45]
# maximo, minimo = obtener_max_y_min(precios)
# print(f'Precio Maximo {maximo}\nPrecio Minimo {minimo}')





# poblacion_mundial = {
#     (19.4326, -99.1332) : 1431414,
#     (35.6895, 139.6917) : 786536,
# }

# print(f'La poblacion de peru es {poblacion_mundial[(35.6895, 139.6917)]}')




# ----------------------------------------------------------




# Ejercicio
# magina que estás construyendo una aplicación que se conecta a diferentes servicios (base de datos, API externa, etc.). Cada servicio tiene una configuración fija: (host, puerto, timeout). Tu tarea es gestionar estas configuraciones.

# Tu Misión:

# Crea una lista llamada servicios_config que contenga tres tuplas. Cada tupla representará la configuración de un servicio:

# Servicio 1 (Base de Datos): ("db.midominio.com", 5432, 5)

# Servicio 2 (API de Pagos): ("api.pagos.com", 443, 10)

# Servicio 3 (Servicio de Logs): ("logs.midominio.com", 1514, 3)

# Escribe una función llamada probar_conexiones que reciba esta lista de configuraciones.

# Dentro de la función, itera sobre la lista. Para cada tupla de configuración, desempaquétala en las variables host, puerto y timeout.

# Dentro del bucle, imprime un mensaje simulando la conexión, que diga:
# "Conectando a {host} en el puerto {puerto} con un timeout de {timeout} segundos..."

# Al final, la función debe devolver una tupla con dos valores: el número total de servicios configurados y el puerto más alto de todas las configuraciones.


# servicios_config = [("db.midominio.com", 5432, 5),
#                     ("api.pagos.com", 443, 10),
#                     ("logs.midominio.com", 1514, 3)]


# def probar_conexion(servicios):
#     print('---Iniciamos prueba de conexion---\n')

#     puerto_mas_alto = 0 

#     for host,puerto,timeout in servicios:
#         print(f'Conectado a {host} en el puerto {puerto} con un timeout de {timeout} segundos....')

#         if puerto > puerto_mas_alto:
#             puerto_mas_alto = puerto

#     total_servicios = len(servicios)

#     print('Finalizar prueba.')

#     return (total_servicios,puerto_mas_alto)
    

# resumen = probar_conexion(servicios_config)
# total, puerto_max = resumen


# print(f"\nResumen: Se configuraron {total} servicios.")
# print(f"El puerto más alto utilizado es: {puerto_max}")














# ---------------------------------------------------------


# Cuando tienes una tupla como ("db.midominio.com", 5432, 5), siempre tienes que recordar que el índice [0] es el host, el [1] es el puerto, etc. Esto puede causar errores si te equivocas de índice.

# Una tupla nombrada (namedtuple) te permite acceder a los elementos por un nombre, como si fuera un objeto (config.host, config.puerto). ¡Es mucho más claro y seguro!

# Tu Nuevo Reto:

# Importa namedtuple desde el módulo collections: from collections import namedtuple

# Crea una "plantilla" para tus tuplas de configuración. La sintaxis es: NombrePlantilla = namedtuple('NombrePlantilla', ['campo1', 'campo2', 'campo3']). Llámala Configuracion y sus campos deben ser host, puerto y timeout.

# Recrea tu lista servicios_config, pero esta vez, cada elemento debe ser una instancia de tu nueva namedtuple Configuracion. Por ejemplo: Configuracion("db.midominio.com", 5432, 5).

# Modifica tu función probar_conexiones para que, en lugar de usar índices, acceda a los datos usando los nombres de los campos (ej: servicio.host, servicio.puerto).



from collections  import namedtuple

Configuracion = namedtuple('Configuracion', ['host', 'puerto', 'timeout'])

servicio_config_1 = Configuracion("db.midominio.com", 5432, 5)
servicio_config_2 = Configuracion("api.pagos.com", 443, 10)
servicio_config_3 = Configuracion("logs.midominio.com", 1514, 3)

lista_de_servicios = [servicio_config_1, servicio_config_2,servicio_config_3]

def probar_coneccion(servicio):

    puerto_mayor = 0

    for servicio in lista_de_servicios:
        print(f'Conectado a {servicio.host} en el puerto {servicio.puerto} con un timeout de {servicio.timeout} segundos....')

    
        if servicio.puerto > puerto_mayor:
            puerto_mayor = servicio.puerto

    numero_de_servicios = len(lista_de_servicios)

    return (numero_de_servicios,puerto_mayor)

prueba = probar_coneccion(Configuracion)
servicios, puerto_mayor = prueba
print(f'El numero de servidos son: {servicios}\nEl puerto mayor es: {puerto_mayor}')



Persona = namedtuple("Persona", ["nombre", "edad", "ciudad"])
p1 = Persona("Ana", 25, "Lima")
for campo in p1._fields:
    print(campo, ":", getattr(p1, campo))
