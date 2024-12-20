import sys
import numpy as np

class Numerica:
    """
    Clase para realizar operaciones numéricas como calcular errores y obtener epsilon de la máquina.
    """

    def __init__(self):
        self.resultado_aproximado = None  # Almacena el último resultado aproximado calculado.

    @staticmethod
    def obtener_epsilon():
        """
        Devuelve el epsilon de la máquina.
        """
        return sys.float_info.epsilon

    def calcular_error(self, valor_real, texto_respuesta):
        """
        Calcula el error absoluto y relativo dado un valor real y una respuesta aproximada.

        Args:
            valor_real (float): El valor exacto conocido.
            texto_respuesta (str): Texto con la solución aproximada en el formato 'y = valor'.

        Returns:
            tuple: Error absoluto y error relativo (en porcentaje).
        """
        try:
            y_aprox = float(texto_respuesta.split("y = ")[1])  # Extraer y
            self.resultado_aproximado = y_aprox
            error_absoluto = abs(valor_real - y_aprox)  # Calcular error absoluto
            error_relativo = (error_absoluto / abs(valor_real)) * 100  # Calcular error relativo
            return error_absoluto, error_relativo
        except Exception as e:
            raise ValueError(f"Error al calcular los errores: {e}")
        
    @staticmethod
    def lower_error(x, e):
        """
        Encuentra el valor más cercano a x en términos de error relativo en un rango alrededor de x.
        Args:
            x (float): Valor objetivo.
            e (float): Margen de error para definir el rango [x-e, x+e].
        Returns:
            float: El valor dentro del rango con menor error relativo.
        """
        if e <= 0:
            raise ValueError("El margen de error (e) debe ser mayor que cero.")
    
        relative_error = float('inf')  # Inicializamos con infinito
        aprox_better = None

        # Itera sobre el rango definido con un paso fijo
        for i in np.arange(x - e, x + e, 0.2):
            if i == 0:  # Evitar división por cero
                continue
            relative_error_new = abs(i - x) / abs(i)
            if relative_error_new < relative_error:
                relative_error = relative_error_new
                aprox_better = i

        if aprox_better is None:
            raise ValueError("No se encontró un mejor aproximado. Verifique los parámetros.")
    
        return aprox_better