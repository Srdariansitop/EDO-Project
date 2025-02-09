from numerica import Numerica
from Function import Function
from Interpolation import Interpolation
import sympy as sym
import matplotlib.pyplot as plt
def test_runge_kutta():
    """
        Corre tests para el metodo runge kutta, 
        y determina si las respuestas estan en un rango esperado
        Tests:
        - Lineal
        - Exponencial
        - Trigonometrica
    """
    test_cases = [
        # Basic Linear Function
        {
            'f': 'x + y',
            'x0': 0, 'y0': 1,
            'h': 0.1,
            'xi': 1,
            'expected_range': (1.5, 2.5)
        },
        # Exponential Function
        {
            'f': 'y',
            'x0': 0, 'y0': 1,
            'h': 0.1,
            'xi': 1,
            'expected_range': (2.7, 2.8)
        },
        # Trigonometric Function
        {
            'f': 'cos(x) + sin(y)',
            'x0': 0, 'y0': 0,
            'h': 0.1,
            'xi': 1,
            'expected_range': (0.5, 1.5)
        }
    ]
    for case in test_cases:
        try:
            f = Function(case['f'])
            result = Numerica.runge_kutta_4(
                f, case['x0'], case['y0'],
                case['h'], case['xi']
            )

            # Chequear si respuesta en rango esperado
            final_y = result[-1][1]
            assert case['expected_range'][0] <= final_y <= case['expected_range'][1], \
                f"Test failed for {case['f']}: {final_y} not in {case['expected_range']}"
            
            print(f"Test passed for {case['f']}")
        except Exception as e:
            print(f"Test failed for {case['f']}: {e}")
    
def test_graph():
    """
    Corre tests para el metodo grafico, 
    y determina si el grafico funcion
    Tests:
    - Lineal
    - Exponencial
    - Trigonometrica
    """
    test_cases = [
        # Basic Linear Function
        {
            'f': 'x + y',
            'x0': 0, 'y0': 1,
            'h': 0.1,
            'xi': 1,
        },
        # Exponential Function
        {
            'f': 'y',
            'x0': 0, 'y0': 1,
            'h': 0.1,
            'xi': 1,
        }
    ]
    for case in test_cases:
        try:
            f = Function([case['f']])
            points = Numerica.runge_kutta_4(
                f, case['x0'], case['y0'],
                case['h'], case['xi']
            )

            # Test if graphic works
            plt.figure()
            x_vals, y_vals = zip(*points)
            plt.plot(x_vals, y_vals)
            plt.title(f"Test Plot for {case['f']}")
            plt.close() # Closing

            print(f"Graphic test passed for {case['f']}")
        except Exception as e:
            print(f"Graphic test failed for {case['f']}: {e}")
    

def test_interpolation():
    """
    Corre tests para el metodo de interpolacion, 
    y determina si el polinomio funciona y checkea precision
    Tests:
    - 4 puntos
    - 3 puntos
    """
    test_cases = [
        {
            'xi': [0, 1, 2, 3],
            'fi': [1, 3, 2, 5],
            'test_point': 1.5
        },
        {
            'xi': [0, 2, 4],
            'fi': [0, 4, 16],
            'test_point': 3
        }
    ]
    for case in test_cases:
        try:
            # Calcular polinomio
            poly = Interpolation.calculate_newton_method(
                case['xi'], case['fi']
            )

            # Testear evaluacion
            x = sym.Symbol('x')
            f = sym.lambdify(x, poly, 'numpy')

            # Chequear precision
            for x_val, f_val in zip(case['xi'], case['fi']):
                assert abs(f(x_val) - f_val) < 1e-10, \
                    f"Interpolation failed at point {x_val}"
            
            print("Interpolation successful")
        except Exception as e:
            print(f"Interpolation test failed: {e}")
