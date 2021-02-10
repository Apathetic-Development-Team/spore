import os
import archive
from sys import argv

gc = '\033[92m'
end = '\033[0m'

def main():
    print(gc + "~*~ Spore ~*~" + end)
    try:
        user_input = argv[1]
        print("User Input: " + user_input)
        archive.process(user_input)
    except:
        print("Usage: main.py yourfile")
        quit()

if __name__ == "__main__":
    main()