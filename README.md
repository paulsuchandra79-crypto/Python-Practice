def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_s = ''.join(s.split()).lower()
    
    # Compare the cleaned string to its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage
input_str = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_str):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
