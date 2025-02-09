import math
import sympy

class Function:
  def __init__(self, function_string):
    if isinstance(function_string, str):
      replacements = {
      "sin": "math.sin",
      "cos": "math.cos",
      "exp": "math.exp",
      "log": "math.log",
      "e": "math.e",
      "^": "**" 
      }
      functionstring = function_string.lower()
      for original, replacement in replacements.items():
        functionstring = functionstring.replace(original, replacement)
    self.function_string = functionstring


    

  def evaluate(self, x, y = None):
    if isinstance(self.function_string, str):
      function_string = self.function_string


      # Dictionary of local variables
      local_vars = {'x': x, 'y': y}

      # Debuggueo
      # print(f"Result of evaluating {function_string} with x = {x} and y = {y}")
      # print(f"Is {eval(function_string, {"math": math}, local_vars)}")

      return eval(function_string, {"math": math}, local_vars)
    elif isinstance(self.function_string, sympy.Expr):
      return self.function_string.subs({'x': x, 'y': y} if y is not None else {'x': x})
    

  
