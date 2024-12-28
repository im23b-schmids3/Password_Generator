import string
import random


# Generates a random password
def generate_password(amount_characters):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(amount_characters))
    return password
