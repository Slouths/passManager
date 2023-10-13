import random
import string


def generate_password(length, numbers = True, special = True):
    characters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    return special


def replay():
    run = input("Do you want to run the program again? ")
    if run == ["y", "yes"]:
        return True
    return False

while True:
    print("Welcome to your password generator!")

    try:
        length = int(input("How many characters do you want your password to be? "))
    except Exception:
        print("Please enter a valid length")
        length = int(input("How many characters do you want your password to be? "))

    nums = input("Do you want your password to include numbers? Y/N ").lower()

    if nums == ["y", "yes", "ye"]:
        nums = True
    elif nums == ["n", "no", "nah"]:
        nums = False
    else:
        print("Please enter a valid letter (Y / N)")
        nums = input("Do you want your password to include numbers? ").lower()
    

    special = input("Do you want your password to include special characters? Y/N ").lower()

    if nums == ["y", "yes", "ye"]:
        nums = True
    elif nums == ["n", "no", "nah"]:
        nums = False
    else:
        print("Please enter a valid letter (Y / N)")
        special = input("Do you want your password to include special characters? ").lower()

    print(generate_password(length, nums, special))

    if replay():
        continue
    else:
        break
    
    
    
    

