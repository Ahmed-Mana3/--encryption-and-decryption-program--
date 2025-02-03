# encrypts and decrypts messages using a random key
import random
import string

alpha = string.ascii_letters + string.digits + string.punctuation + " "
alpha = list(alpha)
key = alpha.copy()

random.shuffle(key)

is_running = True

while is_running:
    choice = input("Do you want to encrypt or decrypt? (e/d): ")


# Encryption

    if choice == "e":
        chars = input("Enter your message: ")
        encrypted = []

        for i in chars:
            encrypted.append(key[alpha.index(i)])

        print("*********************************")
        print("Encrypted Message is: ", end="")
        for letter in encrypted:
            print(letter, end="")
        print()
        print("*********************************")


# Decryption


    elif choice == "d":
        chars = input("Enter your message: ")
        original = []

        for i in chars:
            original.append(alpha[key.index(i)])

        print("*********************************")
        print("Original Message is: ", end="")
        for letter in original:
            print(letter, end="")
        print()
        print("*********************************")

    else:
        print("Invalid input. Please enter 'e' or 'd'.")

    again = input("Do you want to decrypt / encrypt again? (y/n): ")

    if again == "n":
        is_running = False

print("Good Bye")
    

    
