import time


def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(
            f"La funcion demore '{func.__name__}' tardo {fin - inicio:.4f} segundos.")
        return resultado
    return wrapper


@medir_tiempo
def proceso_lento(segundos):
    print(f"Durmiendo por {segundos} segundos(s)")
    time.sleep(segundos)
    print("despierto!")
    return "Tarea completada"

@medir_tiempo
def crear_lista_grande(n):
    print(f"Creando una lista de {n} numeros.")
    lista = list(range(n))
    print("Lista creada!")
    return 'Fin de la creacion '



print(proceso_lento(2))
print('-' * 30)
print(crear_lista_grande(20000000))
