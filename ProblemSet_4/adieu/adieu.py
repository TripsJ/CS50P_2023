import inflect

def main():
    names = []
    while True:
        try:
            names.append(input())
        except EOFError:
            break;

    e = inflect.engine()
    print(f"Adieu, adieu, to {e.join(names)}")






if __name__ == "__main__":
    main()