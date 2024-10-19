import streamlit as st
import hashlib
import string
import random  # Importing the random module

# Function to generate hashes for different algorithms
def generate_hash(word, algorithm):
    if algorithm == "SHA1":
        return hashlib.sha1(word.encode()).hexdigest()
    elif algorithm == "MD5":
        return hashlib.md5(word.encode()).hexdigest()
    elif algorithm == "SHA256":
        return hashlib.sha256(word.encode()).hexdigest()
    elif algorithm == "SHA512":
        return hashlib.sha512(word.encode()).hexdigest()
    # Placeholder for BCRYPT (for demonstration purposes only)
    elif algorithm == "BCRYPT":
        return word  # In a real scenario, you'd use a library like bcrypt to hash the password

# Function to apply masking to a hash (simple XOR masking)
def mask_hash(hash_value):
    # Simple XOR masking with a predefined key (for demonstration)
    key = "my_secret_key"
    masked_hash = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(hash_value))
    return masked_hash

# Function to crack a hash
def crack_hash(hash_to_crack, hash_type):
    pass_found = False
    with open("file.txt", "r") as file:
        for guess in file:
            hashed_guess = generate_hash(guess.strip(), hash_type)
            if hashed_guess.upper() == hash_to_crack.upper():
                return guess.strip()  # Return the cracked password
    return None  # Return None if no match found

# Password strength checking function
def check_password_strength(password):
    length = len(password)
    if length < 8:
        return "Weak", "red"
    elif length < 12:
        return "Moderate", "yellow"
    elif (any(char.isdigit() for char in password) and
          any(char.isalpha() for char in password) and
          any(char in string.punctuation for char in password)):
        return "Strong", "green"
    else:
        return "Moderate", "yellow"

# Function to generate a stronger password suggestion
def suggest_stronger_password(password):
    suggestions = []

    # Create a strong version of the original password
    suggestions.append(password.replace('a', '@').replace('e', '3').replace('i', '1').replace('o', '0').replace('s', '$'))

    # Generate a strong random password of length between 12 to 16 characters
    strong_password = ''.join(random.choices(
        string.ascii_letters + string.digits + string.punctuation,
        k=random.randint(12, 16)
    ))
    suggestions.append(strong_password)

    # Create a complex version of the original password
    complex_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(len(password) + 4))
    suggestions.append(complex_password)

    return suggestions

# Main Streamlit app
st.set_page_config(page_title="Password Security Tools", layout="wide")

# Navigation Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a Page", ["Password Cracker", "Hash Finder", "Password Strength Checker"])

# Password Cracker Page
if page == "Password Cracker":
    st.title("🔒 Password Cracker")
    
    hash_type = st.selectbox("Select Hash Type", ["SHA1", "MD5", "SHA256", "SHA512"])
    hash_to_crack = st.text_input("Enter the hash to crack")

    if st.button("Crack Hash"):
        if hash_to_crack:
            cracked_password = crack_hash(hash_to_crack, hash_type)
            if cracked_password:
                st.success(f"The password is: **{cracked_password}**")
            else:
                st.error("Password not found in database.")

# Hash Finder Page
elif page == "Hash Finder":
    st.title("🔍 Hash Finder")
    st.subheader("Generate Hashes")
    
    algorithms = ["SHA1", "MD5", "SHA256", "SHA512", "BCRYPT"]
    hash_algorithm = st.selectbox("Choose Hash Algorithm", algorithms)
    word = st.text_input("Enter the word to hash")
    
    show_masked_hash = st.checkbox("Show Masked Hash")
    
    if st.button("Generate Hash"):
        if word:
            original_hash = generate_hash(word, hash_algorithm)
            st.success(f"{hash_algorithm} hash for '{word}': {original_hash}")

            # Display masked hash if the checkbox is selected
            if show_masked_hash:
                masked_hash = mask_hash(original_hash)
                st.success(f"Masked hash for '{word}': {masked_hash}")
                
                # Show the description about masking only when the checkbox is checked
                st.write("""
                ### About Masking
                Masking is a technique used to obscure the original hash value. 
                By using masking, even if someone obtains the hashed value, they won't be able to reverse-engineer it back to the original word.
                """)

# Password Strength Checker Page
elif page == "Password Strength Checker":
    st.title("🔑 Password Strength Checker")
    
    password_to_check = st.text_input("Enter a Password to Check Strength")

    if password_to_check:
        strength, color = check_password_strength(password_to_check)
        st.write(f"Password strength: **{strength}**", unsafe_allow_html=True)
        st.markdown(
            f'<span style="color: {color};">{strength}</span>',
            unsafe_allow_html=True
        )
        
        # Display a horizontal bar mapping strength
        if strength == "Weak":
            st.progress(0.33)
            suggestions = suggest_stronger_password(password_to_check)
            st.write("Suggestions for a stronger password:")
            for suggestion in suggestions:
                st.write(f"- **{suggestion}**")
        elif strength == "Moderate":
            st.progress(0.66)
        elif strength == "Strong":
            st.progress(1.0)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("This tool demonstrates various password-related features and aims to educate on password security.")
