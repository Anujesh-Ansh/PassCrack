from pyfiglet import figlet_format

def print_art(msg, font):
    # Generate ASCII art using the chosen font
    ascii_art = figlet_format(msg, font=font)
    print(ascii_art)
    
    # Append the ASCII art to a file
    with open("ascii_art_output.txt", "a") as file:
        file.write(ascii_art + "\n")

# Ask the user for the input message
msg = input("What would you like to print? ")

# Display font options and ask for the user's choice
print("Choose a font option: ")
print("1 -> standard")
print("2 -> cybermedium")
print("3 -> big")
print("4 -> univers")
print("5 -> isometric3")

# Map the user's choice to the corresponding font
font_options = {
    "1": "standard",
    "2": "cybermedium",
    "3": "big",
    "4": "univers",
    "5": "isometric3"
}

choice = input("Enter the number corresponding to the font: ")

# Check if the user's input is valid
if choice in font_options:
    selected_font = font_options[choice]
    # Call the function to print and save the ASCII art
    print_art(msg, selected_font)
else:
    print("Invalid choice. Please select a valid option next time.")