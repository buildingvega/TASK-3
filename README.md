🔐 Random Password Generator

A Random Password Generator built using Python as part of my Oasis Infobyte Internship. This project generates strong and secure passwords based on user-selected criteria through a simple and user-friendly GUI.

📌 Project Overview

The application allows users to create random passwords by selecting the desired password length and character types. It uses Python's secrets module for secure password generation and provides a password strength indicator.

✨ Features

🔢 Password length selection from 8 to 64 characters

🔠 Uppercase letters (A-Z)

🔡 Lowercase letters (a-z)

🔢 Numbers (0-9)

🔣 Symbols ( !@#$... )

🔐 Cryptographically secure password generation using secrets

✅ Ensures at least one character from every selected type

💪 Password strength indicator:

Weak

Medium

Strong


🚫 Option to exclude ambiguous characters such as 0, O, o, 1, I, l

📋 Copy generated password to clipboard

🔄 Generate multiple passwords without restarting

📝 Displays the last 5 generated passwords

⚠️ Input validation

🖥️ Simple graphical user interface using Tkinter


🛠️ Technologies Used

Python

Tkinter – GUI development

Secrets – Secure random password generation

String – Character sets

Pyperclip – Clipboard integration


📂 Project Structure

Random-Password-Generator/
│
├── password_generator.py
└── README.md

🔒 Security

This project uses Python's secrets module instead of the random module for password generation.

The generated password is guaranteed to contain at least one character from each selected character category.

Password history is maintained only during the current session and is not saved to a file.

🎯 Internship Task

Internship: Oasis Infobyte
Project: Random Password Generator
Task: Task 3 – Random Password Generator
Language: Python
Level: Advanced

This project was developed to demonstrate practical knowledge of Python, GUI development, secure random generation, input validation, and clipboard integration.

🚀 Future Improvements

🌙 Dark mode

👁️ Password visibility toggle

🔣 Custom symbol selection

📊 Advanced password strength meter

⚙️ More customization options

🔐 Entropy-based password strength calculation


👨‍💻 Author

Sumit Kumar Patel

B.Tech CSE – 2nd Year
School of Management Sciences, Lucknow
