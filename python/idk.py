import os
import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def check_input(data):
    try:
        if data == "":
            data = 1800
            print(bcolors.OKGREEN + "Default time set to: 1800" + bcolors.ENDC)
            return data
        else:
            data = int(data)
            return data
    except ValueError:
        print(bcolors.FAIL + "\nPlease enter a number" + bcolors.ENDC)

        main()


def main():
    import pyautogui as gui
    print(bcolors.OKGREEN + "How long do you want to sleep? (in seconds)" + bcolors.ENDC)
    print(bcolors.WARNING + "3600 = 1 HOUR \n86400 = 1 DAY" + bcolors.ENDC)
    print(bcolors.OKBLUE + bcolors.BOLD + "DEFAULT = 1800" + bcolors.ENDC)
    time_in_seconds = input()
    time_checked = check_input(time_in_seconds)

    time_in_seconds = time_checked

    for i in range(time_in_seconds):
        time.sleep(1)
        print(i+1)

    gui.click(x=300, y=300)
    exit()


if __name__ == "__main__":
    os.system("xhost +")
    main()
