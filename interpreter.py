from parser import Parser

nonetype = {"type": "None", "value": "None"}

class Interpreter:
    def __init__(self):
        pass
    def eval_program(self, ast):
        latest = nonetype
        for stmt in ast["body"]:
            latest = self.eval_stmt(stmt)
        return latest["value"]
    
    def eval_stmt(self, stmt):
        if stmt["type"] == "NumberLiteral":
            return { "type": "number", "value": stmt["value"], "dtype": stmt["dtype"]}
        elif stmt["type"] == "StringLiteral":
            return { "type": "string", "value": stmt["value"]}
        elif stmt["type"] == "BinaryExpression":
            value = self.eval_binary_expr(stmt)
        elif stmt["type"] == "Program":
            value = self.eval_program(stmt)
        else:
            raise Exception(f"Unknown statement type: {stmt['type']}")
        return value
    
    def eval_binary_expr(self, expr):
        left = self.eval_stmt(expr["left"])
        right = self.eval_stmt(expr["right"])
        # check if both are numbers
        if left["type"] == "number" and right["type"] == "number":
            return self.eval_binary_expr_int(expr["operator"], left, right)
        elif left["type"] == "string" or right["type"] == "string":
            return self.eval_binary_expr_str(expr["operator"], left, right)
        return nonetype
    
    def eval_binary_expr_int(self, op, left_v, right_v):
        value = nonetype
        left = left_v["value"]
        right = right_v["value"]
        dtype = left_v["dtype"]
        if op == "+":
            value = left + right
        elif op == "-":
            value = left - right
        elif op == "*":
            value = left * right
        elif op == "/":
            value = left // right
        elif op == "%":
            value = left % right
        else:
            raise Exception(f"Unknown operator: {op}")
        return { "type": "number", "value": value, "dtype": dtype}
    
    
    def eval_binary_expr_str(self, op, left_v, right_v):
        value = ""
        left = left_v["value"]
        right = right_v["value"]
        ogRType = right_v["type"]

        if type(left) == int:
            left = str(left)
        if type(right) == int:
            right = str(right)
        if op == "+":
            value = left + right
        elif op == "-":
            value = left.replace(right, "")
        elif op == "*":
            if ogRType == "number":
                value = left * int(right)
            else:
                raise Exception(f"Cannot multiply string by string")
        elif op == "/":
            raise Exception(f"Cannot divide string by string")
        return { "type": "string", "value": value}
