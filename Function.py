import math

class Function:
  def __init__(self, function_string):
    self.function_string = function_string

  def evaluate(self, x, y):
    function_string = self.function_string.replace("sin", "math.sin")
    function_string = function_string.replace("cos", "math.cos")
    return eval(function_string)
  
func = Function("sin(x) + y")  # Define la función como 'x**2 + 3*y'
result = func.evaluate(0, 6)  # Evalúa la función en x = 2, y = 5
print(f"f(2, 5) = {result}") # Imprime el resultado (f(2, 5) = 19)