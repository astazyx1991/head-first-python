vowels = ['w', 's', 'x', 'y', 'l']
word = input("enter a word for search vowels")

found = []

for letter in word:
    if letter in vowels:
        found.append(letter)

for vowel in found:
    print(vowel)