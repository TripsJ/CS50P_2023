def main():

    try:
        list ={}
        while True:
            item = input("").upper()
            if item in list:
                list[item] += 1
            else:
                list[item] = 1
    except EOFError:
        # print("\n \n")
        for key, value in sorted(list.items()) :
            print (f"{value} {key}")




if __name__ == "__main__":
    main()