def main():
    print(f"x is {get_int()}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")


main()
