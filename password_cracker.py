from urllib.request import hashlib
import colorama
from colorama import Fore, Style

# Initialize Colorama for colored output in the terminal.
colorama.init()
print(Fore.GREEN + Style.BRIGHT)

# Display the project title in a decorative format.
print(r" ____                                     _ ")
print(r"|  _ \ __ _ ___ _____      _____  _ __ __| |")
print(r"| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |")
print(r"|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |")
print(r"|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|")
print(r"                                            ")
print(r"  ____                _             ")
print(r" / ___|_ __ __ _  ___| | _____ _ __ ")
print(r"| |   | '__/ _` |/ __| |/ / _ \ '__|")
print(r"| |___| | | (_| | (__|   <  __/ |   ")
print(r" \____|_|  \__,_|\___|_|\_\___|_|    ")
print(Style.RESET_ALL)

while True:
    # Prompt the user to select the type of hash to crack or exit the script.
    print()
    print("Enter Type of Hash to be cracked (Select 3 to quit the script)!\n 1. SHA1 Hash \n 2. MD5 Hash \n 3. Quit Script")
    print()
    k = input(">")

    if k == "1":
        passFound = False

        # Get the SHA1 hash from the user.
        sha1hash = input("Please input the SHA1 hash to crack.\n>")

        # Open the file containing potential passwords.
        with open("file.txt", "r") as file:
            # Iterate through each password guess.
            for guess in file:
                # Hash the current guess and compare it to the user-provided hash.
                hashedGuess = hashlib.sha1(bytes(guess.strip(), 'utf-8')).hexdigest()

                if hashedGuess.upper() == sha1hash.upper():
                    # If a match is found, print the password and set the flag.
                    print("The password is ", str(guess))
                    passFound = True
                    break
                else:
                    print("Password guess ", str(guess), " does not match, trying next...")

        # Inform the user if the password was not found.
        if not passFound:
            print("Password not in database, we'll get them next time.")

    elif k == "2":
        passFound = False

        # Get the MD5 hash from the user.
        md5hash = input("Please input the MD5 hash to crack.\n>")

        # Open the file containing potential passwords.
        with open("file.txt", "r") as file:
            # Iterate through each password guess.
            for guess in file:
                # Hash the current guess and compare it to the user-provided hash.
                hashedGuess = hashlib.md5(bytes(guess.strip(), 'utf-8')).hexdigest()

                if hashedGuess.upper() == md5hash.upper():
                    # If a match is found, print the password and set the flag.
                    print("The password is ", str(guess))
                    passFound = True
                    break
                else:
                    print("Password guess ", str(guess), " does not match, trying next...")

        # Inform the user if the password was not found.
        if not passFound:
            print("Password not in database, we'll get them next time.")

    elif k == "3":
        # Exit the script.
        quit()
