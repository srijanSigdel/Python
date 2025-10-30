import string
import random

def generate_strong_password():
    # For characters
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    all_chars = letters + digits + specials

    # Random length between 16 and 64
    length = random.randint(16, 64)

    # Ensure at least one of each category
    password = [random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice(digits),random.choice(specials)]

    # Fill remaining chars
    password += [random.choice(all_chars) for _ in range(length - 4)]

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return "".join(password)

print("Generated strong password:",generate_strong_password())