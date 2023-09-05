import re

def main():
    expr = input("Expression: ")
    if "+" in expr:
        tokens = expr.split("+")
        #print(tokens)
        print (float(tokens[0]) + float(tokens[1]))

    elif "-" in expr:
        tokens = expr.split("-")
        #print(tokens)
        print (float(tokens[0]) - float(tokens[1]))

    elif "*" in expr:
        tokens = expr.split("*")
        #print(tokens)
        print (float(tokens[0]) * float(tokens[1]))

    elif "/" in expr:
        tokens = expr.split("/")
        #print(tokens)
        print (float(tokens[0]) / float(tokens[1]))

    else:
        print("invalid symbol")



main()