vowels = ['w','s','x','y','l']
word = "milliways"

found = []

for letter in word:
    if letter in vowels:
        found.append(letter)

for vowel in found:
    print(vowel)