import random


def main():
    level = get_level()
    points = 10
    round = 0

    while round <= 9:
        tries = 0
        x = generate_integer(level)
        y = generate_integer(level)
        solution = x + y
        while tries <= 2:
            z = input(f"{x} + {y} = ")
            if not z.isnumeric() or int(z) != solution:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(f"{x} + {y} = {solution}")
                    points = points - 1
                    tries += 1
                    round += 1
            else:
                round += 1
                break

    print(f"Points: {points}")


def get_level():
    acceptedLevels = ["1", "2", "3"]
    while True:
        i = input("Level: ")
        if i in acceptedLevels:
            return int(i)
        else:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
