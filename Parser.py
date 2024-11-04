from abc import ABC, abstractmethod
from typing import Optional
from typing import List
from enum import Enum
import math

# TokenType
class TokenType(Enum):
    SUM = "sum"
    SUB = "sub"
    DIV = "div"
    MULT = "mult"
    POW = "pow"
    SIN = "sin"
    COS = "cos"
    TAN = "tan"
    COT = "cot"
    LOG = "log"
    NUM = "num"
    VARIABLE = "variable"
    OPEN_PAREN = "openParan"
    CLOSED_PAREN = "closedParan"
    COMMA = ","
    
# Token
class Token:
    def __init__(self, value: str, token_type: TokenType, column: int):
        self.type = token_type
        self.value = value
        self.column = column

# Utils
class Utils:
    x: float = 0
    y: float = 0
    errors: List[str] = []

    @staticmethod
    def operate(num1: float, num2: float, token: 'Token') -> float:
        if token.type == TokenType.SUM:
            return num1 + num2
        
        elif token.type == TokenType.SUB:
            return num1 - num2
        
        elif token.type == TokenType.MULT:
            return num1 * num2
        
        elif token.type == TokenType.POW:
            return num1 ** num2
        
        elif token.type == TokenType.DIV:
            if num2 != 0:
                return num1 / num2
            else:
                Utils.errors.append(f"Attempted to divide by '0'. Character: {token.column}")
        
        return 0.0

    @classmethod
    def not_errors(cls) -> bool:
        return len(cls.errors) == 0

    @classmethod
    def reset(cls):
        cls.x = 0
        cls.y = 0
        cls.errors.clear()

# Abstarct Class
class IExpression(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass

class Expression(IExpression):
    def __init__(self):
        self.term = None
        self.expressions = None
        self.token = None

    def evaluate(self) -> float:
        if self.expressions is None:
            return self.term.evaluate()
        else:
            return Utils.operate(self.term.evaluate(), self.expressions.evaluate(), self.token)

class Term(IExpression):
    def __init__(self):
        self.factor = None
        self.terms = None
        self.token = None

    def evaluate(self) -> float:
        if self.terms is None:
            return self.factor.evaluate()
        else:
            return Utils.operate(self.factor.evaluate(), self.terms.evaluate(), self.token)

class Factor(IExpression):
    def __init__(self):
        self.token = None
        self.functions = None
        self.expression = None

    def evaluate(self) -> float:
        if self.functions is not None:
            return self.functions.evaluate()
        
        elif self.expression is not None:
            return self.expression.evaluate()
        
        else:
            if self.token.type == TokenType.NUM:
                return float(self.token.value)
            
            elif self.token.type == TokenType.VARIABLE:
                if self.token.value == "x":
                    return Utils.x
                elif self.token.value == "y":
                    return Utils.y
            
            Utils.errors.add(f"'{self.token.value}' has not been declared")
        
        return -1.0
 
# Functions
class Functions(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass
    
class Sin(Functions):
    def __init__(self):
        self.expression = None
    
    def evaluate(self) -> float:
        return math.sin(self.expression.evaluate())

class Cos(Functions):
    def __init__(self):
        self.expression = None
    
    def evaluate(self) -> float:
        return math.cos(self.expression.evaluate())

class Tan(Functions):
    def __init__(self):
        self.expression = None
    
    def evaluate(self) -> float:
        return math.tan(self.expression.evaluate())

class Cot(Functions):
    def __init__(self):
        self.expression = None
        
    def evaluate(self) -> float:
        value = self.expression.evaluate()
        return (math.cos(value)/math.sin(value))

class Log(Functions):
    def __init__(self):
        self.base = None   
        self.arg = None
        
    def evaluate(self) -> float:
        currentBase = self.base.evaluate()
        currentArg = self.arg.evaluate()
        if currentBase > 0 and currentBase != 1:
            if currentArg > 0:
                return math.log(self.base.evaluate, self.arg.evaluate)
            else:
                Utils.errors.append("The argument of the logarithm is not well-defined")
        else:
            Utils.errors.append("The base of the logarithm is not well-defined")
                
# Parser
class Parser:
    
    # Properties
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.index = -1

    # Auxiliar Methods
    def throw_error(self, message: str):
        Utils.errors.append(f"It was expected '{message}'. Character: {self.current().column + 1}")
        self.index += 1

    def look(self) -> Optional[Token]:
        if self.index + 1 < len(self.tokens):
            return self.tokens[self.index + 1]
        else:
            return None
        
    def current(self) -> Token:
        return self.tokens[self.index]
    
    def lookTypes(self, *next_types: TokenType) -> bool:
        lookahead = self.look()
        if lookahead is None:
            return False
        else:
            for token in next_types:
                if token == lookahead.type:
                    return True
        return False
    
    def match(self) -> Token:
        self.index += 1
        token = self.tokens[self.index]
        return token

    # Principal Methods
    def GetFunction(self) -> Expression:
        return self.ExpressionBuilder()

    # Trigonometry
    def SinBuilder(self) -> Sin:
        sin = Sin()
        if self.lookTypes(TokenType.OPEN_PAREN):
            self.match()
            sin.expression = self.ExpressionBuilder()
            
            if self.lookTypes(TokenType.CLOSED_PAREN):
                self.match()
            else:
                self.throw_error(")")
        else:
            self.throw_error("(")
        return sin

    def CosBuilder(self) -> Cos:
        cos = Cos()
        if self.lookTypes(TokenType.OPEN_PAREN):
            self.match()
            cos.expression = self.ExpressionBuilder()
            
            if self.lookTypes(TokenType.CLOSED_PAREN):
                self.match()
            else:
                self.throw_error(")")
        else:
            self.throw_error("(")
        return cos

    def TanBuilder(self) -> Tan:
        tan = Tan() 
        if self.lookTypes(TokenType.OPEN_PAREN):
            self.match()
            tan.expression = self.ExpressionBuilder()
            
            if self.lookTypes(TokenType.CLOSED_PAREN):
                self.match()
            else:
                self.throw_error(")")
        else:
            self.throw_error("(")
        return tan
    
    def CotBuilder(self) -> Cot:
        cot = Cot() 
        if self.lookTypes(TokenType.OPEN_PAREN):
            self.match()
            cot.expression = self.ExpressionBuilder()
            
            if self.lookTypes(TokenType.CLOSED_PAREN):
                self.match()
            else:
                self.throw_error(")")
        else:
            self.throw_error("(")
        return cot
    
    def LogBuilder(self) -> Log:
        log = Log()
        if(self.lookTypes(TokenType.OPEN_PAREN)):
            self.match()
            log.base = self.ExpressionBuilder() # Base
            
            if(self.lookTypes(TokenType.COMMA)): # Comma
                self.match()
            else:
                self.throw_error(",")
            
            log.arg = self.ExpressionBuilder()  # Arg
            
            if(self.lookTypes(TokenType.CLOSED_PAREN)):
                self.match()
            else:
                self.throw_error(")")
        else:
            self.throw_error("(")
        
        return log
        
    
    # Binary's Expressions
    def ExpressionBuilder(self) -> Expression:
        expression = Expression()
        expression.term = self.TermBuilder()
        if self.lookTypes(TokenType.SUM, TokenType.SUB):
            expression.token = self.match()
            expression.expressions = self.ExpressionBuilder()
        return expression

    def TermBuilder(self) -> Term:
        term = Term()
        term.factor = self.FactorBuilder()
        if self.lookTypes(TokenType.DIV, TokenType.MULT, TokenType.POW):
            term.token = self.match()
            term.terms = self.TermBuilder()
        return term

    def FactorBuilder(self) -> Factor:
        factor = Factor()
        
        if self.lookTypes(TokenType.SIN):
            self.match()
            factor.functions = self.SinBuilder()
            
        elif self.lookTypes(TokenType.COS):
            self.match()
            factor.functions = self.CosBuilder()
            
        elif self.lookTypes(TokenType.TAN):
            self.match()
            factor.functions = self.TanBuilder()
        
        elif self.lookTypes(TokenType.COT):
            self.match()
            factor.functions = self.CotBuilder()
        
        elif self.lookTypes(TokenType.LOG):
            self.match()
            factor.functions = self.LogBuilder()
            
        elif self.lookTypes(TokenType.OPEN_PAREN):
            self.match()
            factor.expression = self.ExpressionBuilder()
            
            if self.lookTypes(TokenType.CLOSED_PAREN):
                self.match()
            else:
                self.throw_error(")")
                
        elif self.lookTypes(TokenType.NUM, TokenType.VARIABLE):
            factor.token = self.match()
            
        else:
            self.throw_error("a factor")

        return factor


def main():
    print("Hola")
    
    tokens = [
        Token("cos", TokenType.COS, 0),
        Token("(", TokenType.OPEN_PAREN, 1),
        Token("x", TokenType.VARIABLE, 2),
        Token(")", TokenType.CLOSED_PAREN, 3),
        Token("+", TokenType.SUM, 4),
        Token("2", TokenType.NUM, 5),
        Token("*", TokenType.MULT, 6),
        Token("(", TokenType.OPEN_PAREN, 7),
        Token("y", TokenType.VARIABLE, 8),
        Token("+", TokenType.SUM, 9),
        Token("1", TokenType.NUM, 10),
        Token(")", TokenType.CLOSED_PAREN, 11)
    ]
    # Crear parser
    parser = Parser(tokens)

    # Obtener función
    function = parser.GetFunction()
    Utils.x = 0
    Utils.y = 2
    # Evaluar la función
    result = function.evaluate()
    print(result)
    print("Finish")

if __name__ == "__main__":
    main()
 

