# REVERSE A STRING AND CHECK IF ITS A PALINDROME

word = input("Enter the word :")
rev_word = word[::-1]
print("Reverse of the string is :", rev_word)
if word.lower() == rev_word.lower():
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
