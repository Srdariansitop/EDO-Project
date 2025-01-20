import math
import sympy

class Function:
  def __init__(self, function_string):
    self.function_string = function_string

  def evaluate(self, x, y = None):
    if isinstance(self.function_string, str):
      function_string = self.function_string.replace("sin", "math.sin")
      function_string = function_string.replace("cos", "math.cos")

      # Dictionary of local variables
      local_vars = {'x': x, 'y': y}
      return eval(function_string, {"math": math}, local_vars)
    elif isinstance(self.function_string, sympy.Expr):
      return self.function_string.subs({'x': x, 'y': y} if y is not None else {'x': x})
    

  
