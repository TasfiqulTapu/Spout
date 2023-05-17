import sys
from parser import Parser
from interpreter import Interpreter

def main():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        data = ""
        with open(filename, 'r') as f:
            data = f.read()
        parser = Parser()
        ast = parser.createAST(data)
        print(ast)
    else:
        parser = Parser()
        interpreter = Interpreter()
        print("Spout REPL v0.1.alpha")
        while True:
            interpreter = Interpreter()
            data = input(">>> ")
            if data == "exit":
                break
            out = interpreter.eval_program(parser.createAST(data))
            print(out)

           


if __name__ == "__main__":
    main()