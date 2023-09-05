import string;
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    firstnumberfound = False
    if 1<len(s)<7 and s[0].isalpha() and s[1].isalpha():
        for l in s:
            if l in string.punctuation :
                return False
            if l.isnumeric() and not firstnumberfound:
                if l == "0":
                    return False;
                else:
                    firstnumberfound = True
            if firstnumberfound and l.isalpha():
                return False
        return True
    else:
        return False










main()
