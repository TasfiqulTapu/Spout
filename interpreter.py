from parser import Parser
from environment import defineUndefined
from whale import render

class Interpreter:
    def __init__(self, env):
        self.env = env
    def eval_program(self, ast):
        latest = defineUndefined()
        for stmt in ast["body"]:
            if stmt:
                latest = self.eval_stmt(stmt, self.env, False)
        return latest["value"]
    
    def eval_stmt(self, stmt, env, whale):
        if stmt["type"] == "NumericLiteral":
            return { "type": "number", "value": stmt["value"], "dtype": stmt["dtype"]}
        elif stmt["type"] == "StringLiteral":
            return { "type": "string", "value": stmt["value"]}
        elif stmt["type"] == "Identifier":
            value = self.eval_identifier(stmt, env)
        elif stmt["type"] == "BinaryExpression":
            value = self.eval_binary_expr(stmt,env, whale)
        elif stmt["type"] == "AssignmentExpression":
            name = stmt["left"]["value"]
            value = self.eval_stmt(stmt["right"],env, whale)
            env.assign(name, value)
        elif stmt["type"] == "VariableDeclaration":
            name = stmt["name"]
            value = self.eval_stmt(stmt["value"],env, whale)
            isConst = stmt["const"]
            env.declare(name, value, isConst)
        elif stmt["type"] == "WhalingExpression":
            value = self.eval_stmt(stmt["value"],env, True)
        elif stmt["type"] == "Program":
            value = self.eval_program(stmt,env)
        else:
            raise Exception(f"Unknown statement type: {stmt['type']}\n{stmt}")
        return value
    
    def eval_identifier(self, stmt, env):
        return env.retrive(stmt["value"])

    def eval_binary_expr(self, expr, env, whale):
        left = self.eval_stmt(expr["left"],env, whale)
        right = self.eval_stmt(expr["right"],env, whale)
        # check if both are numbers
        if left["type"] == "number" and right["type"] == "number":
            return self.eval_binary_expr_int(expr["operator"], left, right, whale)
        elif left["type"] == "string" or right["type"] == "string":
            return self.eval_binary_expr_str(expr["operator"], left, right)
        return defineUndefined()
    
    def eval_binary_expr_int(self, op, left_v, right_v, whale):
        value = defineUndefined()
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
        elif op == "**":
            value = left ** right
        elif op == "<<":
            value = left << right
        elif op == ">>":
            value = left >> right
        elif op == "&":
            value = left & right
        elif op == "|":
            value = left | right
        elif op == "^":
            value = left ^ right
        else:
            raise Exception(f"Unknown operator: {op}")
        
        if whale:
            render(op, value, left, right)
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
