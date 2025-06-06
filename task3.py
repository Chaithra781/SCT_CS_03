import re

def assess_password_strength(password):
    score = 0
    criteria = {
        "Length >= 8": len(password) >= 8,
        "Contains uppercase letter": bool(re.search(r'[A-Z]', password)),
        "Contains lowercase letter": bool(re.search(r'[a-z]', password)),
        "Contains digit": bool(re.search(r'\d', password)),
        "Contains special character": bool(re.search(r'[^A-Za-z0-9]', password)),
    }

    print("\nPassword Strength Report:")
    for criterion, passed in criteria.items():
        print(f"- {criterion}: {'✔️' if passed else '❌'}")
        score += int(passed)

    # Overall assessment
    if score == 5:
        strength = "Strong 💪"
    elif 3 <= score < 5:
        strength = "Moderate 🔐"
    else:
        strength = "Weak ⚠️"

    print(f"\nOverall Strength: {strength}")

def main():
    password = input("Enter your password to check strength: ")
    assess_password_strength(password)

if __name__ == "__main__":
    main()
