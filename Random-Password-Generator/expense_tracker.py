# ==============================
#   RANDOM PASSWORD GENERATOR
# ==============================

import random
import string

print("===================================")
print("   Random Password Generator")
print("===================================")

while True:
    try:
        length = int(input("Enter password length (minimum 6): "))

        if length < 6:
            print("Password must be at least 6 characters long!")
            continue
        break

    except ValueError:
        print("Please enter a valid number!")

# Ask user whether to include special characters
choice = input("Include special characters? (yes/no): ").lower()

characters = string.ascii_letters + string.digits

if choice == "yes":
    characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\n========== Result ==========")
print("Generated Password:", password)

# Password Strength
if length >= 12:
    print("Password Strength: Strong")
elif length >= 8:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")

print("============================")
