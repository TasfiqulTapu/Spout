from lexer import TokenType, Lexer, parseInt

class Parser:
    # have a private token list
    def __init__(self):
        self.tokens = []

    def notEOF(self):
        return self.tokens[0]["type"] != TokenType.EOF
    
    def consume(self):
        popped = self.tokens.pop(0)
        return popped
    
    def peek(self):
        return self.tokens[0]

    def expect(self, type):
        if self.peek()["type"] == type:
            return self.consume()
        else:
            raise Exception("Expected " + type + " but got " + self.peek()["type"])

    def createAST(self, sourceCode):
        self.tokens = Lexer(sourceCode)
        ast = {
            "type": "Program",
            "body": []
        }
        while(self.notEOF()):
            ast["body"].append(self.parse_stmt())
        
        return ast

    def parse_stmt(self):
        return self.parse_expr()

    def parse_expr(self):
        return self.parse_additive_expr()

    def parse_additive_expr(self):
        left = self.parse_multiplicative_expr()
        while self.peek()["value"] == "+" or self.peek()["value"] == "-":
            op = self.consume()
            right = self.parse_multiplicative_expr()
            left = {
                "type": "BinaryExpression",
                "operator": op["value"],
                "left": left,
                "right": right
            }
        return left
    
    def parse_multiplicative_expr(self):
        left = self.parse_primary_expr()
        while self.peek()["value"] == "*" or self.peek()["value"] == "/" or self.peek()["value"] == "%":
            op = self.consume()
            right = self.parse_primary_expr()
            left = {
                "type": "BinaryExpression",
                "operator": op["value"],
                "left": left,
                "right": right
            }
        return left
    
    def parse_primary_expr(self):
        curr = self.peek()["type"]
        if curr == TokenType.Number:
            num = parseInt(self.consume()["value"])
            return {
                "type": "NumberLiteral",
                "value": num["value"],
                "base": num["base"],
                "dtype": "int"
            }
        elif curr == TokenType.String:
            return {
                "type": "StringLiteral",
                "value": self.consume()["value"],
                "dtype": "string"
            }
        elif curr == TokenType.OpenParen:
            self.consume()
            expr = self.parse_expr()
            self.expect(TokenType.CloseParen)
            return expr
        else:
            raise Exception("Unexpected token " + self.peek()["value"])
        





        
