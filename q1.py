
# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength of the password. 

# ●       Implement a Python function called check_password_strength that takes a password string as input.

# ●       The function should check the password against the following criteria:

# ○       Minimum length: The password should be at least 8 characters long.

# ○       Contains both uppercase and lowercase letters.

# ○       Contains at least one digit (0-9).

# ○       Contains at least one special character (e.g., !, @, #, $, %).

# ●       The function should return a boolean value indicating whether the password meets the criteria.

# ●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

# ●       Provide appropriate feedback to the user based on the strength of the password.  

import re


def check_password_strength(password):
    
    lowercase_pattern = re.compile(r'[a-z]')
    uppercase_pattern = re.compile(r'[A-Z]')
    digit_pattern = re.compile(r'\d')
    specialchar_pattern = re.compile(r'[!@#$%]')
    
    if len(password) < 8:
        return False
    if lowercase_pattern.search(password) is None:
        return False
    if uppercase_pattern.search(password) is None:
        return False
    if digit_pattern.search(password) is None:
        return False
    if specialchar_pattern.search(password) is None:
        return False
    return True

if __name__ == "__main__":
    
    user_password = input ("Enter a password to check its strength: ")
    
    if check_password_strength(user_password):
        print("Your password is strong.")
    else:
        print("Your password is weak. Please ensure it meets all the criteria.")
    
    
    
