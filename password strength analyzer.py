# =============================================================================
# Password Strength Analyzer
# Author: Alejandro Camacho
# Course: CYB-333 Security Automation
# Description: This program checks how strong a password is based on
#              length, character types, and common password patterns.
# =============================================================================

import re

# A list of commonly used and breached passwords to check against
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123", "password1",
    "111111", "iloveyou", "admin", "letmein", "monkey", "1234567",
    "sunshine", "master", "dragon", "654321", "superman", "michael",
    "football", "shadow", "password123", "123123", "welcome", "login",
    "passw0rd", "starwars", "hello", "charlie", "batman", "freedom",
    "ninja", "mustang", "access", "flower", "rockyou", "cheese"
]


def check_length(password):
    # Checks if the password is long enough
    # Returns a score and feedback message
    length = len(password)
    if length >= 16:
        return 3, None
    elif length >= 12:
        return 2, "Try using 16 or more characters for better security."
    elif length >= 8:
        return 1, "Password is too short. Use at least 12 characters."
    else:
        return 0, "Password is way too short. Use at least 12 characters."


def check_character_types(password):
    # Checks if the password uses a mix of character types
    # Awards one point for each type found
    score = 0
    feedback = []

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers (0-9).")

    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    else:
        feedback.append("Add special characters like !, @, #, or $.")

    return score, feedback


def check_common_password(password):
    # Checks if the password is on the known breached passwords list
    if password.lower() in COMMON_PASSWORDS:
        return True, "This password is on a known breached passwords list. Do not use it."
    return False, None


def check_repeated_characters(password):
    # Checks for three or more repeated characters in a row (like 'aaa' or '111')
    if re.search(r'(.)\1{2,}', password):
        return True, "Avoid repeating the same character three or more times in a row."
    return False, None


def check_common_patterns(password):
    # Checks for simple patterns like 'abc', '123', or 'qwerty'
    patterns = ["abc", "123", "234", "345", "456", "567", "678", "789",
                "qwerty", "asdf", "zxcv", "qaz", "wsx"]
    lower = password.lower()
    for pattern in patterns:
        if pattern in lower:
            return True, "Avoid simple patterns like 'abc', '123', or 'qwerty'."
    return False, None


def analyze_password(password):
    # Runs all checks and calculates a final score and rating
    # Strong: 6 or more points
    # Moderate: 4 to 5 points
    # Weak: 3 points or less

    score = 0
    feedback = []

    # Run length check
    length_score, length_feedback = check_length(password)
    score += length_score
    if length_feedback:
        feedback.append(length_feedback)

    # Run character type check
    type_score, type_feedback = check_character_types(password)
    score += type_score
    feedback.extend(type_feedback)

    # Run common password check
    is_common, common_feedback = check_common_password(password)
    if is_common:
        score -= 2
        feedback.append(common_feedback)

    # Run repeated characters check
    has_repeats, repeat_feedback = check_repeated_characters(password)
    if has_repeats:
        score -= 1
        feedback.append(repeat_feedback)

    # Run common patterns check
    has_pattern, pattern_feedback = check_common_patterns(password)
    if has_pattern:
        score -= 1
        feedback.append(pattern_feedback)

    # Determine the rating based on total score
    if score >= 6:
        rating = "Strong"
    elif score >= 4:
        rating = "Moderate"
    else:
        rating = "Weak"

    return score, rating, feedback


def show_results(password, score, rating, feedback):
    # Displays the results in a clean, readable format
    print("\n" + "=" * 50)
    print("     PASSWORD STRENGTH ANALYSIS REPORT")
    print("=" * 50)
    print(f"  Password : {'*' * len(password)}")
    print(f"  Score    : {score}")
    print(f"  Rating   : {rating}")
    print("-" * 50)

    if feedback:
        print("  Suggestions to improve your password:")
        for item in feedback:
            print(f"    - {item}")
    else:
        print("  Great job! No issues found.")

    print("=" * 50 + "\n")


def main():
    # Main function that runs the program
    print("\n" + "=" * 50)
    print("       PASSWORD STRENGTH ANALYZER")
    print("       CYB-333 | Alejandro Camacho")
    print("=" * 50)
    print("Type 'quit' to exit.\n")

    while True:
        password = input("Enter a password to analyze: ").strip()

        if password.lower() == "quit":
            print("\nExiting. Goodbye\n")
            break

        if not password:
            print("No password entered. Please try again.\n")
            continue

        score, rating, feedback = analyze_password(password)
        show_results(password, score, rating, feedback)


# Start the program
if __name__ == "__main__":
    main()