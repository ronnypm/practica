def sumar (a:int, b:int):
    return sum([a,b])

def restar(a:int, b:int):
    restar_a_b = a- b 
    return restar_a_b

if __name__ == '__main__':

    print("--- Realizando prueba interna de la calculadora ---")
    resultado_prueba = sumar(10, 5)
    print(f"Resultado de la prueba (10 + 5): {resultado_prueba}")


    