import string
from random import *

MIN = int(input("Minimum length: "))
MAX = int(input("Maximum length: "))

def main():
    try:
        if MIN > MAX:
            print("\nMinimum length must be less than maximum length.")
        else:
            characters = string.ascii_letters + string.punctuation  + string.digits
            password =  "".join(choice(characters) for x in range(randint(MIN, MAX)))
            print (password)

    except:
        print("\nAn error has occured. Please try again.")

if __name__ == "__main__":
    main()