class Interpolation:

    def divided_difference(self, points):
        """
        Calculate the divided differences coefficients for the
        set of data x and y. Returns: list: List of divided
        differences coefficients.
        """
        n = len(points) - 1
        table = [[points[i][1]] for i in range(n)]
    
        for j in range(1, n):
            row = []
            for i in range(n-j):
                next_row = [(table[i][j-1] - table[i+1][j-1]) / (points[i+j+1][0] - points[i][0])]
                row.extend([table[i][k] for k in range(j)])
                row.append(next_row[0])
            table.append(row)
        return table

    def calculate_newton_method(self):
        """
        Newton's method for interpolation Darío...
        """
        pass

