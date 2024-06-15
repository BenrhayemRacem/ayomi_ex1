import re


class RpnService:

    def evaluate(self, expression: str = None, seperator: str = " "):
        if expression is None:
            raise ValueError("Expected an expression , got None")
        tokens = expression.split(seperator)
        stack = []
        steps = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        for token in tokens:
            if token in operators:
                if len(stack) < 2:
                    raise ValueError("Malformed expression")
                b = stack.pop()
                a = stack.pop()
                if token == "/" and b == 0:
                    raise ZeroDivisionError("Division by zero")
                result = operators[token](a, b)
                steps.append(f"{a} {token} {b} = {result}")
                stack.append(result)
            else:
                try:
                    stack.append(float(token))
                except ValueError:
                    raise ValueError(f"Invalid token: {token}")

        if len(stack) != 1:
            raise ValueError("Malformed expression")

        final_result = stack[0]
        return final_result, steps

    def validate(self,expression: str, seperator: str = " "):
        if not re.match(r"^[\d\s+\-*/]+$", expression):
            raise ValueError("Expression contains invalid characters")
        tokens = expression.split(seperator)
        operators = {"+", "-", "*", "/"}
        num_count = 0
        op_count = 0
        for token in tokens:
            if token in operators:
                op_count += 1
            else:
                num_count += 1
        if op_count >= num_count:
            raise ValueError("Malformed expression")
