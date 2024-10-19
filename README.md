# 🛡️ Password Security Tools 🔐


## 🌟 Overview
Welcome to the **Password Security Tools** project! This suite of tools is designed to enhance your password security practices. It includes a **Password Cracker**, **Hash Finder**, **Password Strength Checker**, and a **Masking** feature to demonstrate how to protect sensitive password data effectively.

## 🚀 Features

### 1. 🔑 Password Cracker
- **Functionality**: Input a hash value, select the hash type, and attempt to find the corresponding password from a predefined list of passwords stored in a text file.
- **Supported Hash Types**: 
  - SHA1
  - MD5
  - SHA256
  - SHA512
  - BCRYPT (demonstration purposes only)

### 2. 🕵️ Hash Finder
- **Functionality**: Enter a word and select a hashing algorithm to generate its corresponding hash.
- **Masking Option**: Optionally generate a masked version of the hash that obscures the original hash value.
- **About Masking**: Masking is a technique used to obscure the original hash, making it difficult to reverse-engineer. 🛡️

### 3. 💪 Password Strength Checker
- **Functionality**: Input a password to check its strength based on criteria such as length, and character variety (letters, numbers, and special characters).
- **Strength Ratings**: 
  - Weak 🚫
  - Moderate ⚠️
  - Strong 💪
- **Suggestions**: Generates stronger password suggestions if the entered password is deemed weak. ✨

## 📦 Installation

### Prerequisites
- Python 3.x 🐍
- Streamlit 🌐
- Required libraries: `hashlib`, `string`, `random`

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/Password_Security_Tools.git
   cd Password_Security_Tools
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required libraries**:
   ```bash
   pip install streamlit
   ```

## 🛠️ Usage
1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your web browser** and navigate to `http://localhost:8501`. 🌍

3. **Choose the desired tool** from the navigation sidebar and follow the on-screen instructions. 📋

## 📁 File Structure
```
Password_Security_Tools/
│
├── app.py                # Main application script
├── file.txt              # Text file containing potential passwords for cracking
├── README.md             # This README file
└── requirements.txt      # This includes the packages and libraries necessary for the program to run
```

## 🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request. 💡

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments
- Special thanks to the open-source community for the libraries and tools that made this project possible. 🎉

Happy coding! 🐍💻✨