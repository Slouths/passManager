import random
import string
import streamlit as st


#Function that generates a password based on the parameters.
def generate_password(length, numbers=False, special=False):

    characters = list(string.ascii_letters)
    digits = list(string.digits)
    special_chars = list(string.punctuation)

    if not numbers and not special:
        # If the user doesn't want numbers or special characters, use only letters
        available_chars = characters
    elif numbers and special:
        # If the user wants both numbers and special characters
        available_chars = characters + digits + special_chars
    elif numbers:
        # If the user wants only numbers
        available_chars = characters + digits
    else:
        # If the user wants only special characters
        available_chars = characters + special_chars

    password = "".join(random.choice(available_chars) for _ in range(length))

    return password

    # Streamlit app
st.title("Random Password Generator")

length = st.slider("Select password length", 6, 20, 8)  # Change the range as needed
include_numbers = st.checkbox("Include numbers")
include_special_chars = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = generate_password(length, include_numbers, include_special_chars)
    st.write("Generated Password:", password)

