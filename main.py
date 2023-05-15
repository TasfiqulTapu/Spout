import sys

def main():
    filename = sys.argv[1]
    data = ""
    with open(filename, 'r') as f:
        data = f.read()
    lex = Lexer(data)
    print(lex)


def Lexer(data):
    lexical = []
    #automatic newline insertion
    string = data.replace(";", "\n")
    symbols = ["=", "+", "-", "*", "/", "%", "(", ")", "'","\"", "&", "|", "^", "~", "!", "<", ">", "\n",","]

    lexed = []
    temp = ""
    skipnext = False
    for i,char in enumerate(string):
        if skipnext:
            skipnext = False
            continue
        if char != " ":
            temp += char
        if (i+1 < len(string)):
            if temp == "/" and string[i+1] == "/":
                lexed.append("<comment>")
                temp = ""
                skipnext = True
            if string[i+1] == " " or string[i+1] in symbols or temp in symbols:
                if temp == "\n":
                    temp = "<newline>"
                if temp != "":
                    lexed.append(temp)  
                temp = ""
    return lexed
            


if __name__ == "__main__":
    main()