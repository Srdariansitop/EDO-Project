import math

class Function:
  def __init__(self, function_string):
    self.function_string = function_string

  def evaluate(self, x, y):
    function_string = self.function_string.replace("sin", "math.sin")
    function_string = function_string.replace("cos", "math.cos")
    return eval(function_string)
  
