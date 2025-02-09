from numerica import Numerica
from Function import Function
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