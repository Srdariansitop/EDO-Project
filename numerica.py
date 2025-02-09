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

    @staticmethod
    def suma_numerica(*args):
        """
        Recibe uno o más argumentos numéricos, los ordena de menor a mayor y los suma.
        Returns:
        float: La suma de todos los argumentos ordenados de menor a mayor.
        """
        sum_result = 0
        ordered_numbers = sorted(args)
        for num in ordered_numbers:
            sum_result += num
            
        # Debugueo
        # print(f"Resultado de sumar {ordered_numbers} es {sum_result}")

        return sum_result
    
    @staticmethod
    def cercanos(a, b, tol_rel = 1e-9, tol_abs = 0.0):
        """
        Comparacion <= que determina si 2 valores son tan cercanos numericamente,
        que su diferencia es resultado de un error en calculos. Esto se mide usando tolerancias:
        Variables:
        - a, b Valores a comparar
        - tol_rel: Tolerancia relativa
        - tol_abs: Tolerancia absoluta
        Returns:
        - Booleano indicando si los valores son muy cercanos
        """
        return abs(a - b) <= max(tol_rel * max(abs(a), abs(b)), tol_abs)
    
    @staticmethod
    def runge_kutta_4(f, x0, y0, H, xi):
        x, y = x0, y0
        result = [(x, y)]
        while x < xi:
            if Numerica.cercanos(x, xi):
                break
            k1 = H * f.evaluate(x, y)
            k2 = H * f.evaluate(Numerica.suma_numerica(x, H / 2), Numerica.suma_numerica(y, k1 / 2))
            k3 = H * f.evaluate(Numerica.suma_numerica(x, H / 2), Numerica.suma_numerica(y, k2 / 2))
            k4 = H * f.evaluate(Numerica.suma_numerica(x, H), Numerica.suma_numerica(y, k3))
            y = Numerica.suma_numerica(y, Numerica.suma_numerica(k1, 2 * k2, 2 * k3, k4) / 6)
            x = Numerica.suma_numerica(x, H)
            result.append((x, y))
        return result
    








    