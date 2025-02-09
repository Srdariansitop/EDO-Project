import sympy as sym

class Interpolation:
    """
    This class implements the Newton-Gregory method with
    divided differences to create a polynomial that accurately
    represents a set of given data points.
    """

    @staticmethod
    def __divided_difference(points):
        """
        Calculate the divided differences coefficients for the
        set of data points (xi, fi).
        Returns:
            list: A table of divided differences coefficients.
        """
        n = len(points)
        coef = [[0] * n for _ in range(n)]

        # Fill the first column with y values
        for i in range(n):
            coef[i][0] = points[i][1]

        # Calculate divided differences
        for j in range(1, n):
            for i in range(n - j):
                coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (points[i + j][0] - points[i][0])

        return coef

    @staticmethod
    def calculate_newton_method(xi, fi):
        """
        Construct the Newton-Gregory polynomial using the divided differences
        and return the polynomial.
        """
        # Convert xi and fi into a list of points
        points = [(xi[i], fi[i]) for i in range(len(xi))]
        
        # Get the divided differences table
        coef = Interpolation.__divided_difference(points)
        
        # Construct the polynomial
        x = sym.Symbol('x')
        polynomial = coef[0][0]
        
        for i in range(1, len(xi)):
            term = coef[0][i]
            for j in range(i):
                term *= (x - xi[j])
            polynomial += term

        # Expand the polynomial for better readability
        polynomial = sym.expand(polynomial)
        return polynomial
    

