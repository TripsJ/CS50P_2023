def main():
    time = input("What's the time? ").lower().strip()
    convertedTime = convert(time)

    if 7<= convertedTime <= 8:
        print ("breakfast time")
    elif 12<= convertedTime <= 13:
        print("lunch time")
    elif 18<= convertedTime <=19:
        print("dinner time")


def convert(t):
    if ":" in t:
        timetokens = t.split(":")
        return float(timetokens[0]) + (float(timetokens[1])/60)
    else:
        return -1

if __name__ == "__main__":
    main()