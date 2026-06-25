# Password Strength Analyzer

**CYB-333 Security Automation | Alejandro Camacho**

---

## Project Overview

The Password Strength Analyzer is a command-line Python tool that evaluates the strength of a user-provided password. It checks the password against a set of security criteria and common attack patterns, then returns a strength rating along with specific recommendations to help the user improve their password.

This project was built as part of a security automation course to demonstrate how repetitive security tasks, like password policy enforcement, can be handled programmatically and consistently.

---

## Features

- Checks password length
- Checks for character type diversity (uppercase, lowercase, numbers, special characters)
- Detects common and previously breached passwords
- Flags repeated characters (e.g. `aaa`, `111`)
- Detects simple patterns (e.g. `abc`, `123`, `qwerty`)
- Outputs a score, strength rating (Weak, Moderate, or Strong), and improvement suggestions

---

## Requirements

- Python 3.x
- No external libraries required — uses only built-in Python modules

---

## How to Run

1. Clone or download this repository
2. Open a terminal and navigate to the project folder
3. Run the script with the following command:

```bash
python password_strength_analyzer.py
```

4. Enter a password when prompted
5. Review your strength rating and suggestions
6. Type `quit` to exit the program

---

## Example Output

```
==================================================
       PASSWORD STRENGTH ANALYZER
       CYB-333 | Alejandro Camacho
==================================================
Type 'quit' to exit.

Enter a password to analyze: ************

==================================================
     PASSWORD STRENGTH ANALYSIS REPORT
==================================================
  Password : ************
  Score    : 3
  Rating   : Weak
--------------------------------------------------
  Suggestions to improve your password:
    - Try using 16 or more characters for better security.
    - Add uppercase letters (A-Z).
    - Avoid simple patterns like 'abc', '123', or 'qwerty'.
==================================================
```

---

## Scoring System

| Criteria | Points |
|---|---|
| Length 16+ characters | +3 |
| Length 12-15 characters | +2 |
| Length 8-11 characters | +1 |
| Uppercase letters present | +1 |
| Lowercase letters present | +1 |
| Numbers present | +1 |
| Special characters present | +1 |
| Known breached password | -2 |
| Repeated characters (aaa, 111) | -1 |
| Simple patterns (abc, 123, qwerty) | -1 |

| Rating | Score |
|---|---|
| Strong | 6 or more |
| Moderate | 4 to 5 |
| Weak | 3 or less |

---

## File Structure

```
password-strength-analyzer/
│
├── password_strength_analyzer.py   # Main Python script
└── README.md                       # Project documentation
```

---

## Notes

- Passwords are masked with asterisks in the output and are never stored or logged
- The breached password list is a sample set for demonstration purposes
- This tool is intended for educational use as part of a security automation course
