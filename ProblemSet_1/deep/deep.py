def main():
    answer = input ("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    match answer.lower().strip():
        case "42" | "forty two"|"forty-two":
            print("yes")
        case _:
            print("no")

main()