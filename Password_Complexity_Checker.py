def check_password_strength(password):
    """Assess the strength of a password."""
    strength = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "numbers": any(char.isdigit() for char in password),
        "special_characters": any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password),
    }

    # Calculate the strength score
    score = sum(strength.values())

    # Determine the feedback
    if score == 5:
        feedback = "Strong Password! Your password is secure."
    elif score >= 3:
        feedback = "Moderate Password. Consider adding more complexity."
    else:
        feedback = "Weak Password. Try making it longer and adding uppercase, numbers, and special characters."

    return feedback, strength


if __name__ == "__main__":
    print("Password Complexity Checker")
    password = input("Enter a password to check its strength: ").strip()

    feedback, strength = check_password_strength(password)

    print("\nPassword Strength Analysis:")
    print(f"Length >= 8 characters: {'✔' if strength['length'] else '✘'}")
    print(f"Contains uppercase letters: {'✔' if strength['uppercase'] else '✘'}")
    print(f"Contains lowercase letters: {'✔' if strength['lowercase'] else '✘'}")
    print(f"Contains numbers: {'✔' if strength['numbers'] else '✘'}")
    print(f"Contains special characters: {'✔' if strength['special_characters'] else '✘'}")
    print("\nFeedback:")
    print(feedback)
