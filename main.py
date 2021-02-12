import os
import archive
from sys import argv
import gui

gc = '\033[92m'
end = '\033[0m'


def main():
    print(gc + "~*~ Spore ~*~" + end)
    try:
        if len(argv) >= 1:
            user_input = argv[1]
            print("User Input: " + user_input)
            archive.process(user_input)
    except IndexError:
        gui.init()


if __name__ == "__main__":
    main()
