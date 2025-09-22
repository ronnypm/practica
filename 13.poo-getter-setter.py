class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        print("Obteniendo precio")
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        print(f"Asignando nuevo precio {nuevo_precio}")
        self._precio = nuevo_precio

producto = Producto("Tablet", 1500)
producto.precio = 2000

producto.precio = -10