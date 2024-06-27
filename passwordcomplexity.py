import re

def password_strength(password):
    # Initialize strength score
    strength = 0

    # Check for length
    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1

    # Check for special characters
    if re.search(r"\W", password):
        strength += 1

    # Determine password strength based on score
    if strength <= 2:
        return "Weak"
    elif strength <= 4:
        return "Medium"
    else:
        return "Strong"

# Example usage
password=input("enter a password:")
print(password_strength(password))  # Output: Strong
