from enum import Enum, auto

class TokenType(Enum):
    Number = auto()
    Identifier = auto()
    Let = auto()
    Const = auto()
    Whale = auto()
    BinaryOperator = auto()
    UnaryOperator = auto()
    Equals = auto()
    OpenParen = auto()
    ClosePare = auto()
    EOF = auto()

KEYWORDS = {
    "let": TokenType.Let,
    "const": TokenType.Const,
    "whale": TokenType.Whale
}

BinOps = ["+", "-", "*", "/", "%", "&", "|", "^", "<<", ">>", "**"]
UnaOps = ["~"]

def Lexer(data):
    lexical = []
    #automatic newline insertion
    string = data.replace(";", "\n")
    symbols = ["=", "+", "-", "*", "/", "%", "(", ")", "'", "&", "|", "^", "~", "!", "<", ">", "\n",","]

    lexed = []
    temp = ""
    skipline = False
    for i,char in enumerate(string):
        if skipline and char == "\n":
            skipline = False
        if skipline:
            continue
        if char != " " and char != "\t":
            temp += char
        if (i+1 < len(string)):
            if temp == "/" and string[i+1] == "/":
                lexed.append("<comment>")
                temp = ""
                skipline = True
            if string[i+1] == " " or string[i+1] == "\t" or string[i+1] in symbols or temp in symbols:
                if temp == "\n":
                    temp = "<newline>"
                if temp != "":
                    lexed.append(temp)  
                temp = ""
    print(lexed)
    tokens = tokenize(lexed)
    return tokens

def parseInt(value):
    last = ""
    base = 10
    if len(value)>2 and value[0] == "0" and value[1].isalpha():
        last = value[2:]
        if value[1] == 'b':
            base = 2
        elif value[1] == 'o':
            base = 8
        elif value[1] == 'x':
            base = 16
    else:
        last = value
    
    if last.isnumeric():
        return {value: int(last, base), base: base}
    return False
    

def token(value, type):
    return {"value": value, "type": type}

def tokenize(lex):
    tokens = []

    while(len(lex)):
        if lex[0] == "(":
            tokens.append(token(lex.pop(0),TokenType.OpenParen))
        elif lex[0] == ")":
            tokens.append(token(lex.pop(0),TokenType.ClosePare))
        elif lex[0] in BinOps:
            tokens.append(token(lex.pop(0),TokenType.BinaryOperator))
        elif lex[0] == "=":
            tokens.append(token(lex.pop(0),TokenType.Equals))
        else:
            if parseInt(lex[0]):
                tokens.append(token(lex.pop(0), TokenType.Number))

            else:
                reserved = lex[0] in KEYWORDS
                if reserved:
                    tokens.append(token(lex[0], KEYWORDS[lex.pop(0)]))
                else:
                    tokens.append(token(lex.pop(0), TokenType.Identifier))
            

    tokens.append(token("EndOfFile", TokenType.EOF))
    return tokens
            


        










