def main():
    while True:
        userinput = input("Date: ").strip()
        try:
            if verify(userinput):
                break;
        except ValueError:
            pass



def verify(d:str):
    month = [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December"
                ]

    if "/" in d:
        d=d.split("/")
        for e in d:
            if not e.isnumeric():
                return False
    else:
        d= d.split(" ")
        if "," in d[1]:
            d[1] = d[1].rstrip(",")
        else:
            return False

    if len(d) != 3:
        return False
    else:
        if d[0].isnumeric():
            if 0<int(d[0])<13:
                d[0] = f"{int(d[0]):02d}"
            else:
                return False
        elif d[0] in month:
            d[0] = f"{month.index(d[0])+1:02d}"
        else:
            return False




    if 1 > int(d[1]) or int(d[1]) >31:
        return False
    else:
        d[1]=f"{int(d[1]):02d}"
        print(f"{d[2]}-{d[0]}-{d[1]}")
        return True

if __name__ == "__main__":
    main()