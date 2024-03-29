import random
import string
from operator import *
def generate_password(length=12, include_lowercase=True, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = ""
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected for password generation.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password_length = int(input("Enter the desired password length: "))
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

generated_password = generate_password(
length=password_length,
include_lowercase=use_lowercase,
include_uppercase=use_uppercase,
include_digits=use_digits,
include_special_chars=use_special_chars
)

if generated_password:
    print(f"Generated Password: {generated_password}")