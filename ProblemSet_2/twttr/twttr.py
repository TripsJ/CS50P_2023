def main():
    phrase = input("Input: ")
    voyels = "aeiou"
    for letter in phrase:
        if (letter in voyels) or letter in voyels.upper():
            phrase = phrase.replace(letter,"")

    print(f"Output: {phrase}")

main()
