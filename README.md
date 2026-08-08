# SecurePass – Password Strength Analyzer & Secure Password Generator

SecurePass is a Python-based cybersecurity mini project that analyzes password strength and generates secure random passwords.

The application evaluates passwords based on length, character complexity, common password patterns, repeated characters, and sequential characters. It also provides an estimated password entropy and recommendations for improving password security.

## Features

### Password Strength Analyzer

* Password strength score from 0–100
* Weak, Medium, Strong, and Very Strong classifications
* Password length analysis
* Uppercase letter detection
* Lowercase letter detection
* Number detection
* Special character detection
* Common password detection
* Repeated character detection
* Sequential character detection
* Estimated password entropy
* Security recommendations

### Secure Password Generator

* Customizable password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Secure random generation using Python's `secrets` module
* Copy generated password to clipboard

## Technologies Used

* Python
* Tkinter
* Regular Expressions (`re`)
* `secrets`
* `math`

## Project Structure

```text
SecurePass/
│
├── main.py
├── password_checker.py
├── password_generator.py
├── README.md
├── requirements.txt
└── screenshots/
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/SecurePass.git
```

### 2. Navigate to the project directory

```bash
cd SecurePass
```

### 3. Run the application

```bash
python main.py
```

No external Python packages are required because the project uses Python's standard library.

## Example

A weak password such as:

```text
123456
```

can be detected as a commonly used password.

A more complex password such as:

```text
MySecure@2026!Pass
```

will receive a significantly higher strength score.

## Security Note

The password analyzer is intended for educational purposes. The entropy calculation provides an estimate and should not be considered a complete measure of real-world password security.

Users should avoid entering real passwords into demonstration or testing applications.

## Learning Outcomes

This project helped demonstrate practical knowledge of:

* Python programming
* Regular expressions
* GUI development with Tkinter
* Password security concepts
* Input validation
* Secure random generation
* Basic cybersecurity principles

## Future Enhancements

* Password breach checking using a privacy-preserving API
* Password strength visualization
* More extensive common-password detection
* Password policy customization
* Exporting security analysis reports
* Improved modern GUI design
