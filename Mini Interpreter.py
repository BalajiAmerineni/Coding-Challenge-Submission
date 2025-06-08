import re

class MiniInterpreter:
    def __init__(self):
        self.variables = {}

    def evaluate_expression(self, expr: str) -> int:
        """
        Evaluate an arithmetic expression with variables substituted.
        """
       
        for var, val in self.variables.items():
            expr = re.sub(rf'\b{var}\b', str(val), expr)

        try:
           
            return eval(expr, {"__builtins__": {}})
        except Exception as e:
            raise ValueError(f"Invalid expression: {expr}") from e

    def execute(self, line: str) -> int | None:
        """
        Parses and executes a single statement: 'let' or 'if'.
        Returns result for 'if', None for 'let'.
        """
        line = line.strip()

        if line.startswith("let"):
            
            match = re.match(r"let\s+(\w+)\s*=\s*(.+)", line)
            if not match:
                raise SyntaxError("Invalid let statement")
            var, expr = match.groups()
            value = self.evaluate_expression(expr)
            self.variables[var] = value
            return None

        elif line.startswith("if"):
           
            match = re.match(r"if\s+(.+?)\s+then\s+(.+?)\s+else\s+(.+)", line)
            if not match:
                raise SyntaxError("Invalid if statement")
            condition_expr, then_expr, else_expr = match.groups()
            condition_result = self.evaluate_expression(condition_expr)
            return self.evaluate_expression(then_expr if condition_result else else_expr)

        else:
            raise SyntaxError("Unknown statement type")

def test_mini_interpreter():
    interpreter = MiniInterpreter()

    print("Executing: let x = 10")
    interpreter.execute("let x = 10")

    print("Executing: let y = x + 5")
    interpreter.execute("let y = x + 5")

    print("Executing: if y > 10 then y * 2 else y - 2")
    result = interpreter.execute("if y > 10 then y * 2 else y - 2")
    print("Result:", result)  

    print("Executing: if x < 5 then x + 1 else x - 1")
    result = interpreter.execute("if x < 5 then x + 1 else x - 1")
    print("Result:", result)  

if __name__ == "__main__":
    interpreter = MiniInterpreter()

    print(">>> let x = 10")
    interpreter.execute("let x = 10")

    print(">>> let y = x + 5")
    interpreter.execute("let y = x + 5")

    print(">>> if y > 10 then y * 2 else y - 2")
    result = interpreter.execute("if y > 10 then y * 2 else y - 2")
    print("Result:", result)  

    print(">>> if x < 5 then x + 1 else x - 1")
    result = interpreter.execute("if x < 5 then x + 1 else x - 1")
    print("Result:", result)  
