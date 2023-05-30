def is_palindrome(input_string):
    return input_string == input_string[::-1]


# Example usage
base = "racecar"
print(base)
if is_palindrome(base):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

base = "racecars"
print(base)
if is_palindrome(base):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
