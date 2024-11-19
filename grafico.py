import numpy as np
import matplotlib.pyplot as plt

# Función para graficar el campo de isoclinas y la curva solución
def graficar_campo_isoclinas_y_solucion(f, h, puntos_rk, margen=0.2, expansion_isoclinas=5):
    # Extraer los valores de x e y de los puntos de Runge-Kutta
    x_vals, y_vals = zip(*puntos_rk)

    # Calcular dinámicamente los rangos de x e y
    xi, xf = min(x_vals), max(x_vals)
    yi, yf = min(y_vals), max(y_vals)

    # Agregar un margen al rango de los puntos de Runge-Kutta
    rango_x = xf - xi
    rango_y = yf - yi
    xi -= rango_x * margen
    xf += rango_x * margen
    yi -= rango_y * margen
    yf += rango_y * margen

    # Expandir el rango adicionalmente para incluir más espacio de isoclinas
    xi -= expansion_isoclinas
    xf += expansion_isoclinas
    yi -= expansion_isoclinas
    yf += expansion_isoclinas

    # Crear el espacio de valores para x y y
    x = np.arange(xi, xf + h, h)
    y = np.arange(yi, yf + h, h)

    # Crear una malla de coordenadas
    X, Y = np.meshgrid(x, y)

    # Calcular las pendientes para el campo de direcciones
    U = 1  # Componente horizontal de las flechas
    V = f(X, Y)  # Componente vertical de las flechas
    U2, V2 = U / np.sqrt(U**2 + V**2), V / np.sqrt(U**2 + V**2)  # Normalización de la longitud de las flechas

    # Graficar el campo de direcciones (isoclinas)
    plt.quiver(X, Y, U2, V2, color='gray', alpha=0.6)

    # Graficar la curva solución usando los puntos de Runge-Kutta
    plt.plot(x_vals, y_vals, color='blue', label='Solución Runge-Kutta', marker='o')

    # Configuraciones adicionales del gráfico
    plt.title(r'Campo de direcciones y Solución Runge-Kutta')
    plt.xlim(xi, xf)
    plt.ylim(yi, yf)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Línea horizontal en y = 0
    plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Línea vertical en x = 0
    plt.legend()
    plt.show()

# Ejemplo de uso
# def f(x, y):
#     return 2 * y - x

# puntos_rk = [(0, 1), (1, 1.2), (2, 1.5), (3, 2.0)]  # Puntos generados por Runge-Kutta
# h = 1  # Paso
# graficar_campo_isoclinas_y_solucion(f, h, puntos_rk, margen=0.2, expansion_isoclinas=10)
