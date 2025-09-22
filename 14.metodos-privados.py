
# class CalculadoraSimple:
#     def __init__(self):
#         # Esto es público (sin guiones)
#         self.resultado = 0

#     def sumar(self, a, b):
#         numero_a = self.__validar_numero(a)
#         numero_b = self.__validar_numero(b)

#         if numero_a and numero_b:
#             suma = self.__hacer_suma(a, b)
#             texto = self.__mostrar_operacion("+", a, b, suma)
#             self.__guardar_resultado(suma)
#             return texto
#         return "ERROR: números inválidos"

#     def resta(self, a, b):
#         numero_a = self.__validar_numero(a)
#         numero_b = self.__validar_numero(b)

#         if numero_a and numero_b:
#             resta = self.__hacer_resta(a, b)
#             texto = self.__mostrar_operacion("-", a, b, resta)
#             self.__guardar_resultado(resta)
#             return texto
#         return "ERROR: números inválidos"

#     def obtener_ultomo_resultado(self):
#         return self.resultado

#     def __validar_numero(self, numero):
#         if isinstance(numero, (int, float)):
#             return True
#         return False

#     def __hacer_suma(self, a, b):
#         return a + b

#     def __hacer_resta(self, a, b):
#         return a - b

#     def __guardar_resultado(self, valor):
#         self.resultado = valor

#     def __mostrar_operacion(self, operacion, a, b, resultado):
#         return f"{a} {operacion} {b} = {resultado}"


# if __name__ == "__main__":

#     calc = CalculadoraSimple()

#     print(calc.sumar(5, 9))
#     print(calc.resta(10, 5))
#     print(calc.obtener_ultomo_resultado())


# ----------------------------------------------------


class GeneradorReportes:
    def __init__(self, titulo_empresa):
        self.titulo_empresa = titulo_empresa
        self.__contador_reportes = 0

    def _obtener_encabezado(self):
        return f"=== {self.titulo_empresa.upper()} ===\n"

    def _formatear_datos(self, datos):
        """PROTEGIDO: Las clases hijas pueden cambiar cómo se muestran los datos"""
        return "\n".join(f"• {item}" for item in datos)

    def _obtener_pie(self):
        return f"\n--- Fin del reporte ---"

    def __incrementar_contador(self):
        """PRIVADO: Solo esta clase controla el contador"""
        self.__contador_reportes += 1

    def __generar_numero_reporte(self):
        """PRIVADO: Lógica interna para numerar reportes"""
        return f"RPT-{self.__contador_reportes:04d}"

    # ==================== MÉTODO PÚBLICO ====================
    def generar_reporte(self, datos):
        """Método público que coordina todo"""
        self.__incrementar_contador()
        numero = self.__generar_numero_reporte()

        encabezado = self._obtener_encabezado()
        contenido = self._formatear_datos(datos)
        pie = self._obtener_pie()

        return f"{numero}\n{encabezado}{contenido}{pie}"


class ReporteHTML(GeneradorReportes):
    
     def _obtener_encabezado(self):
         return f"HTML: <h1>{self.titulo_empresa}</h1>"
     
     def _formatear_datos(self, datos):
        return '\n'.join([f"<ul><li>{item}</li><ul>" for item in datos])
    
