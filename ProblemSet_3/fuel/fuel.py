def main():
    while True:
        val = input("Insert fraction: " )
        if "/" not in val:
            pass
        else:
            val = val.split("/")
            if len(val) == 2:
                try:

                    result = (int(val[0])/int(val[1]))*100
                    if result > 100:
                        pass
                    elif result >= 99:
                        print("F")
                        break
                    elif result <= 1:
                        print("E")
                        break
                    else:
                        print (f"{result:.0f}%")
                        break
                except ValueError:
                    pass
                except ZeroDivisionError:
                    pass

if __name__ == "__main__":
    main()




