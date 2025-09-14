# Define la Función generar_perfil:

# Debe aceptar un argumento obligatorio: nombre.

# Debe aceptar un número variable de hobbies usando *hobbies.

# Debe aceptar un número variable de redes sociales usando **redes_sociales.

# Lógica Dentro de la Función:

# Imprime el nombre del usuario de forma destacada (ej: --- Perfil de: Ana ---).

# Comprueba si la tupla hobbies contiene algo. Si no está vacía, imprime un encabezado "Hobbies:" y luego cada hobby en una línea.

# Comprueba si el diccionario redes_sociales contiene algo. Si no está vacío, imprime un encabezado "Redes Sociales:" y luego cada red con su usuario (ej: - Twitter: @ana_dev).

# Imprime una línea en blanco al final para separar los perfiles.

# Prueba la Función:

# Llama a tu función generar_perfil varias veces con diferentes datos para probar que funciona en todos los casos:


def generar_perfiles(nombre: int, *args, **kwargs):
    print(f"--- Perfil de: {nombre}")
    if args:
        print('Hobbies')
        for h in args:
            print(h)

    if kwargs:
        print("Redes Sociales")
        for red_social, nombre_usuario in kwargs.items():
            print(f"{red_social.capitalize()} : {nombre_usuario}")


def perfiles_creados():

    generar_perfiles("Alex")
    generar_perfiles("Brenda", "Leer", "Nadar", "Ajedrez") 
    generar_perfiles("Carlos", twitter="@carlos_dev", linkedin="/in/carlos")
    generar_perfiles("Diana", "Correr", "Pintar",
                     instagram="@diana_art", github="/dianacodes")


perfiles_creados()