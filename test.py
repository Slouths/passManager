import random
import string

def rando(charList):
    char = []
    for i in range(len(charList)):
        char.append(str(i))
    return char

characters = rando(string.ascii_letters)

print(characters)