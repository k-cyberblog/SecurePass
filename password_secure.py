import re
import math


COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "admin",
    "password123",
    "letmein",
    "welcome",
    "iloveyou",
    "abc123"
}


def has_repeated_characters(password):
    """Check for 3 or more consecutive repeated characters."""
    return bool(re.search(r"(.)\1\1", password))


def has_sequence(password):
    """Check for simple ascending/descending sequences."""
    sequences = [
        "0123456789",
        "9876543210",
        "abcdefghijklmnopqrstuvwxyz",
        "zyxwvutsrqponmlkjihgfedcba"
    ]

    password_lower = password.lower()

    for sequence in sequences:
        for i in range(len(sequence) - 3):
            part = sequence[i:i + 4]

            if part in password_lower:
                return True

    return False


def calculate_entropy(password):
    """Estimate password entropy in bits."""

    character_pool = 0

    if re.search(r"[a-z]", password):
        character_pool += 26

    if re.search(r"[A-Z]", password):
        character_pool += 26

    if re.search(r"[0-9]", password):
        character_pool += 10

    if re.search(r"[^A-Za-z0-9]", password):
        character_pool += 32

    if character_pool == 0:
        return 0

    entropy = len(password) * math.log2(character_pool)

    return round(entropy, 2)


def check_password(password):

    score = 0
    suggestions = []

    # Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
        suggestions.append("Use at least 12 characters for better security.")
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        suggestions.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 15
    else:
        suggestions.append("Add lowercase letters.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 15
    else:
        suggestions.append("Add numbers.")

    # Special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        suggestions.append("Add special characters such as @, #, or !.")

    # Common password detection
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append(
            "This password is commonly used and should be avoided."
        )

    # Repeated characters
    if has_repeated_characters(password):
        score -= 10
        suggestions.append(
            "Avoid repeating the same character multiple times."
        )

    # Sequential characters
    if has_sequence(password):
        score -= 10
        suggestions.append(
            "Avoid predictable sequences such as 1234 or abcd."
        )

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    # Strength classification
    if score < 40:
        strength = "Weak"
    elif score < 60:
        strength = "Medium"
    elif score < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    # Entropy
    entropy = calculate_entropy(password)

    return score, strength, entropy, suggestions
