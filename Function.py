class Function:
    def __init__(self, function_string):
        self.function_string = function_string

    def evaluate(self, x, y):
        return eval(self.function_string) 

func = Function("x**2 + 3*y")  # Define la función como 'x**2 + 3*y'
result = func.evaluate(2, 5)  # Evalúa la función en x = 2, y = 5
print(f"f(2, 5) = {result}") # Imprime el resultado (f(2, 5) = 19)