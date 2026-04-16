def is_palindrome(s):
    """Checks if the given string is a palindrome."""
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s[::-1] == s 

print(is_palindrome("A man a plan a canal Panama"))  
print(is_palindrome("Hello World"))