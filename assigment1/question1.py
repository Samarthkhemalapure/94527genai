# Take input from user
s = input("Enter a sentence: ")

# Number of characters
NO_Chars = len(s)

# Number of words
words = s.split()
NO_words = len(words)

# Number of vowels
vowels = "aeiouAEIOU"
num_vowels = 0

for char in s:
    if char in vowels:
        num_vowels += 1

# Print results
print("Number of characters:", NO_Chars)
print("Number of words:", NO_words)
print("Number of vowels:", num_vowels)
