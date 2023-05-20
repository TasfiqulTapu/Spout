import sys
import json
from parser import Parser
from interpreter import Interpreter
from environment import Environment, defineNum, defineStr


def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        data = ""
        with open(filename, 'r') as f:
            data = f.read()
        parser = Parser()
        ast = parser.createAST(data)
        if len(sys.argv) >= 3 and sys.argv[2] == "--ast":
            print(json.dumps(ast, indent=2))
        else:
            env = Environment()
            interpreter = Interpreter(env)
            out = interpreter.eval_program(ast)
            print(out)
    else:
        parser = Parser()
        env = Environment()
        # env.declare("x", defineNum("int", 10), False)
        # env.declare("version", defineStr("0.2"), True)
        interpreter = Interpreter(env)
        print("Spout REPL v0.2")
        src = ""
        while True:
            data = input(">>> ") + "\n"
            if data == "exit\n":
                break
            elif data[-2:] == ";\n":
                src += data[:-1]
            else:
                src += data
                ast = parser.createAST(src)
                out = interpreter.eval_program(ast)
                src = ""
                print(out)
                
        

           


if __name__ == "__main__":
    main()