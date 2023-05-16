import sys
from lexer import Lexer


def main():
    filename = sys.argv[1]
    data = ""
    with open(filename, 'r') as f:
        data = f.read()
    lex = Lexer(data)
    print(lex)

           


if __name__ == "__main__":
    main()