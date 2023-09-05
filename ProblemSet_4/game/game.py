from random import randint
import sys

def main():
    l = 0

    while True:
        try:
          level = input ("Level: ")
          if int(level) > 0:
              l = int(level)
              break;
        except ValueError:
            continue


    target =randint(1,l)
    while True:
        try:
            guess = input("Guess: ")
            if int(guess)> target:
                print("Too large!")
            elif int(guess)<target:
                print ("Too small!")
            elif int(guess) == target:
                sys.exit("Just right!")
        except ValueError:
            continue




if __name__ == "__main__":
    main()

