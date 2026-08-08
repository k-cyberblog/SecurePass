import string
import secrets


def generate_password(
    length,
    use_uppercase=True,
    use_lowercase=True,
    use_numbers=True,
    use_special=True
):

    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_numbers:
        character_sets.append(string.digits)

    if use_special:
        character_sets.append("!@#$%^&*()-_=+[]{}")

    if not character_sets:
        raise ValueError("Select at least one character type.")

    all_characters = "".join(character_sets)

    # Make sure the generated password contains
    # at least one character from each selected category.
    password_characters = [
        secrets.choice(characters)
        for characters in character_sets
    ]

    remaining_length = length - len(password_characters)

    if remaining_length < 0:
        raise ValueError(
            "Password length is too short for the selected options."
        )

    for _ in range(remaining_length):
        password_characters.append(
            secrets.choice(all_characters)
        )

    # Securely shuffle the characters
    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)
