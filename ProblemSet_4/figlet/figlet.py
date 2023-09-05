from pyfiglet import Figlet
import sys

def main():
    print (len(sys.argv))
    print (sys.argv[2])
    if (len(sys.argv)== 1):
        i =input("Input: ")
        f = Figlet(font='slant')
        print(f.renderText(i))
    elif (len(sys.argv)==3 and sys.argv[1] =="-f"):
        i =input("Input: ")
        f=Figlet(font=sys.argv[2])
        print(f.renderText(i))
    else:
        sys.exit("Invalid usage")




if __name__ == "__main__":
    main()