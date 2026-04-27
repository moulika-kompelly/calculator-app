import random
import string

# ask user for password length
length = int(input("Enter password length: "))

# all characters
characters = string.ascii_letters + string.digits + string.punctuation

# generate password
password = ""
for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)