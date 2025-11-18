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
    
    
    
