import string
import random

print("Welcome to the Linux User Password Generator!\n")

while True:
    try:
        password_length = int(input("Please enter the desired password length: "))
        if password_length < 4:
            print("The password must be more than 4 characters.")
        else:
            break
    except ValueError:
        print("Incorrect data has been entered. Enter an integer")

password_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation)

while len(password) < password_length:
    password += (random.choice(password_characters))

print("\nGenerated password:", password)