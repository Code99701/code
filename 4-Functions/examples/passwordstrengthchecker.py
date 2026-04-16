def is_strong_password(password):
    """Checks if the given password is strong."""
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        return False
    return True 

## calling the password
print(is_strong_password("weak"))  # False
print(is_strong_password("StrongPass123!"))  # True