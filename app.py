import random
import string

#Function that generates a password based on the parameters.
def generate_password(length, numbers = True, special = True):
    characters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    password = ""
    while len(password) < length:

        password += characters

        if numbers:
            password += characters
        elif special:
            password += special

    return password

#Asks the user if they want to replay the password program
def replay():
    run = input("Do you want to run the program again? ")
    if run == ["y", "yes"]:
        return True
    return False

#Main runs until user does not want to generate anymore passwords
while True:
    print("Welcome to your password generator!")

    #Tries to turn length into an int, if it cant then the user is prompted again
    try:
        length = int(input("How many characters do you want your password to be? "))
    except Exception:
        print("Please enter a valid length")
        length = int(input("How many characters do you want your password to be? "))

    #Gets number option
    nums = input("Do you want your password to include numbers? Y/N ").lower().strip()

    if nums in ["y", "yes", "ye"]:
        nums = True
    elif nums in ["n", "no", "nah"]:
        nums = False
    else:
        print("Please enter a valid letter (Y / N)")
        nums = input("Do you want your password to include numbers? ").lower().strip()
    
    #Gets special character option
    special = input("Do you want your password to include special characters? Y/N ").lower().strip()

    if special in ["y", "yes", "ye"]:
        special = True
    elif special in ["n", "no", "nah"]:
        special = False
    else:
        print("Please enter a valid letter (Y / N)")
        special = input("Do you want your password to include special characters? ").lower().strip()

    #Prints out the password
    print(generate_password(length, nums, special))

    #Checks if user wants to generate another password
    if replay():
        continue
    else:
        break
    
    
    
    

