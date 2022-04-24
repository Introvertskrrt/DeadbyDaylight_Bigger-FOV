import os
import time
import colorama
import webbrowser

from colorama import Fore
from pathlib import Path
home = str(Path.home())
colorama.init()

# Function

def writeFOVSteam():
    with open('Resources\\fov.ini', 'r') as firstfile, open(f'{home}\AppData\Local\DeadbyDaylight\Saved\Config\WindowsNoEditor\Engine.ini', 'a') as secondfile:

        for _string in firstfile:
            secondfile.write(_string)

    return


def writeFOVEGS():
    with open('Resources\\fov.ini', 'r') as firstfile, open(f'{home}\AppData\Local\DeadbyDaylight\Saved\Config\EGS\Engine.ini', 'a') as secondfile:

        for _string in firstfile:
            secondfile.write(_string)

    return

def writeFOVMicrosoft():
    with open('Resources\\fov.ini', 'r') as firstfile, open(f'{home}\AppData\Local\DeadbyDaylight\Saved\Config\grdk\Engine.ini', 'a') as secondfile:

        for _string in firstfile:
            secondfile.write(_string)

    return

def removeFOVSteam():
    with open('Resources\\default.ini', 'r') as firstfile, open(f'{home}\AppData\Local\DeadbyDaylight\Saved\Config\WindowsNoEditor\Engine.ini', 'w') as secondfile:

        for _string in firstfile:
            secondfile.write(_string)

    return

def removeFOVEGS():
    with open('Resources\\default.ini', 'r') as firstfile, open(f'{home}\AppData\Local\DeadbyDaylight\Saved\Config\EGS\Engine.ini', 'w') as secondfile:

        for _string in firstfile:
            secondfile.write(_string)

    return

def removeFOVMicrosoft():
    with open('Resources\\default.ini', 'r') as firstfile, open(f'{home}\AppData\Local\DeadbyDaylight\Saved\Config\grdk\Engine.ini', 'w') as secondfile:

        for _string in firstfile:
            secondfile.write(_string)

    return


def openDiscord():
    url = 'https://discord.gg/suuab4gntN'

    webbrowser.open(url)


# Select Platfrom Menu

def selectPlatfrom():
    print(Fore.RED + 'Bigger FOV Config' + Fore.WHITE)

    print('Select Your Platfrom: ')
    print(f'1. Steam {Fore.BLUE} (Requires SSL Bypass) {Fore.WHITE}')
    print('2. Epic Games')
    print('3. Microsoft Store')

    command = input(">>")

    if command == "1":
        print('Steam Selected')
        time.sleep(1.5)
        print(Fore.GREEN + '\nInstalling Bigger FOV...')
        writeFOVSteam()
        time.sleep(1.5)
        print(Fore.GREEN + 'Bigger FOV Config Installed' + Fore.WHITE)
        os.system('pause')
        openDiscord()

    elif command == "2":
        print('Epic Games Selected')
        time.sleep(1.5)
        print(Fore.GREEN + '\nInstalling Bigger FOV...')
        writeFOVEGS()
        time.sleep(1.5)
        print(Fore.GREEN + 'Bigger FOV Config Installed' + Fore.WHITE)
        os.system('pause')
        openDiscord()

    elif command == "3":
        print('Epic Games Selected')
        time.sleep(1.5)
        print(Fore.GREEN + '\nInstalling Bigger FOV...')
        writeFOVMicrosoft()
        time.sleep(1.5)
        print(Fore.GREEN + 'Bigger FOV Config Installed' + Fore.WHITE)
        os.system('pause')
        openDiscord()

    else:
        print(f"{command} is an Unkown Command!")
        time.sleep(1.5)
        os.system('cls')
        return main()

    return


# Main Program

def main():
    print('Choose what you want to do!\n')
    print('1. Install FOV Config')
    print('2. Remove FOV Config')

    command = input(">>")

    if command == "1":
        os.system('cls')
        selectPlatfrom()

    elif command == "2":
        os.system('cls')
        print("Restore your config to default settings")
        print('1. Steam')
        print('2. Epic Games')
        print('3. Microsoft Store')

        command = input(">>")
        if command == "1":
            print(Fore.GREEN + 'Restoring to default settings...')
            removeFOVSteam()
            time.sleep(1.5)
            print(Fore.MAGENTA + 'Config Restored' + Fore.WHITE)
            os.system('pause')
            openDiscord()

        elif command == "2":
            print(Fore.GREEN + 'Restoring to default settings...')
            removeFOVEGS()
            time.sleep(1.5)
            print(Fore.MAGENTA + 'Config Restored' + Fore.WHITE)
            os.system('pause')
            openDiscord()

        elif command == "3":
            print(Fore.GREEN + 'Restoring to default settings...')
            removeFOVMicrosoft()
            time.sleep(1.5)
            print(Fore.MAGENTA + 'Config Restored' + Fore.WHITE)
            os.system('pause')
            openDiscord()

    else:
        print(f"{command} is an Unkown Command!")
        time.sleep(1.5)
        os.system('cls')
        return main()

main()