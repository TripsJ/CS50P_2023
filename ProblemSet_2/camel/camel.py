def main():
    camelcase = input("CamelCase: ")

    for l in camelcase:
        if l.isupper():
            rep = "_"+l.lower()
            camelcase  = camelcase.replace(l,rep)

    print("snake_case: "+ camelcase)

main()