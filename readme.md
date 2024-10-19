# 🐍 Hash Finder and Cracker 🔍

Welcome to the **Hash Finder** and **Hash Cracker** project! This repository contains two Python scripts that provide functionalities for hashing strings and cracking hashes. Below is a brief overview of each script.

---

## 🛠️ Files Included

### 1. **hash_finder.py** 🔍
This script allows users to generate SHA-1 and MD5 hashes from input strings. It also saves the generated hashes to a file named `hash_output.txt`.

#### Key Features:
- Choose between SHA-1 and MD5 hash generation.
- User-friendly command-line interface.
- Saves results to `hash_output.txt` 📁.

#### Example Usage:
```bash
python hash_finder.py
```
🌟 **Output:** Displays the hash value for the input string.

---

### 2. **cracker.py** 🔓
This script helps users crack SHA-1 and MD5 hashes by comparing them against a list of potential passwords stored in `file.txt`.

#### Key Features:
- Supports cracking both SHA-1 and MD5 hashes.
- Displays attempts and results on the console.
- Reports whether the password was found or not.

#### Example Usage:
```bash
python cracker.py
```
🔑 **Output:** The program will indicate if the password is found or not.

---

## 🚀 Getting Started

To use the scripts, make sure you have Python installed on your machine. You may also need to install the `colorama` package for color support:

```bash
pip install colorama
```

### 🧑‍💻 Running the Scripts
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Password_Cracker.git
   ```
2. Navigate into the directory:
   ```bash
   cd Password_Cracker
   ```
3. Run any of the scripts as needed:
   ```bash
   python hash_finder.py
   python cracker.py
   ```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎉 Acknowledgments
Thanks to the open-source community for providing great libraries like **Colorama**! ❤️

---

## 📞 Contact
For any questions or contributions, feel free to reach out!

---

Happy coding! 🐍💻✨
```

