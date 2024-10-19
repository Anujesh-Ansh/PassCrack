import hashlib
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Print the HASHCODE FINDER banner in red
print(Fore.RED + Style.BRIGHT)
print(r" _   _           _       _____ _           _           ")
print(r"| | | | __ _ ___| |__   |  ___(_)_ __   __| | ___ _ __ ")
print(r"| |_| |/ _` / __| '_ \  | |_  | | '_ \ / _` |/ _ \ '__|")
print(r"|  _  | (_| \__ \ | | | |  _| | | | | | (_| |  __/ |   ")
print(r"|_| |_|\__,_|___/_| |_| |_|   |_|_| |_|\__,_|\___|_|    ")
print(Style.RESET_ALL)  # Reset styles after printing

# Function to generate SHA-1 hash
def generate_sha1(word):
    return hashlib.sha1(word.encode()).hexdigest()

# Function to generate MD5 hash
def generate_md5(word):
    return hashlib.md5(word.encode()).hexdigest()

# Main program loop
while True:
    # Ask user for the hash type
    print("Choose the type of hash:")
    print("1 -> SHA-1")
    print("2 -> MD5")
    print("3 -> Quit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        # Ask user to enter the word
        word = input("Enter the word you want to hash with SHA-1: ")
        hash_value = generate_sha1(word)
        print(Fore.YELLOW + f"SHA-1 hash for '{word}': {hash_value}" + Fore.RESET)
        # Append result to the file
        with open("hash_output.txt", "a") as file:
            file.write(f'"{word}" : "SHA-1" : "{hash_value}"\n')

    elif choice == "2":
        # Ask user to enter the word
        word = input("Enter the word you want to hash with MD5: ")
        hash_value = generate_md5(word)
        print(Fore.YELLOW + f"MD5 hash for '{word}': {hash_value}" + Fore.RESET)
        # Append result to the file
        with open("hash_output.txt", "a") as file:
            file.write(f'"{word}" : "MD5" : "{hash_value}"\n')

    elif choice == "3":
        print(Fore.CYAN + "Exiting the program. Goodbye!" + Fore.RESET)
        break

    else:
        print(Fore.RED + "Invalid choice. Please enter 1, 2, or 3." + Fore.RESET)
