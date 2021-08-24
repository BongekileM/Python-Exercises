# Python program that returns reverse of a string.

def is_palindrome(word):
    return word == word[::-1]


word = input("Please enter a word: ")
answer = is_palindrome(word)  # Function call.

if answer:
    print("true")
else:
    print("false")
