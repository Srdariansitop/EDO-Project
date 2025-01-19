import numpy as np
import sympy as sym


class Interpolation:
    """
    This class implements the Newton-Gregory method with
    divided differences to create a polynomial that accurately
    represents a set of given data points
    """

    @staticmethod
    def __divided_difference(points):
        """
        Calculate the divided differences coefficients for the
        set of data x and y. Returns: list: List of divided
        differences coefficients.
        """
        n = len(points) - 1
        table = [[points[i][1]] for i in range(n)]

        for j in range(1, n):
            row = []
            for i in range(n - j):
                next_row = [(table[i][j - 1] - table[i + 1][j - 1]) / (points[i + j + 1][0] - points[i][0])]
                row.extend([table[i][k] for k in range(j)])
                row.append(next_row[0])
            table.append(row)
        return table

    @staticmethod
    def calculate_newton_method(xi, fi):
        """
        Construct the Newton-Gregory polynomial using the divided differences
        and return polynomial
        """
        points = [i for i in xi], [j for j in fi]
        coef = Interpolation.__divided_difference(points)
        x = sym.Symbol('x')
        polynomial = coef[0][0]
        for i in range(1, len(xi)):
            term = coef[0][i]
            for j in range(i):
                term = term * (x - xi[j])
            polynomial += term

        polynomial = sym.expand(polynomial)
        return polynomial




