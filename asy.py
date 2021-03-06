#!/usr/local/bin/python3
# Chris Farrell - @seajay - https://github.com/seajaysec/
"""
Identifies whether Y is a consonant or vowel in a given word.
"""
y_vowel_state = False
static_vowels = ["A", "E", "I", "O", "U"]
word_up = input("Enter your word: ").upper()
print(f"Entered word is: {word_up}")

if "Y" in word_up:
    print("Y found. Checking vowel status.")
    static_vowel_match = [chars in static_vowels for chars in word_up]
    other_vowel_present = any(static_vowel_match)
    if other_vowel_present == True:
        print("Other vowels identified.")
        if word_up[-1] == "Y":
            y_vowel_state = True
    else:
        print("No other vowels identfied")
        y_vowel_state = True
else:
    print("No Y found.")
    y_vowel_state = False

print(f"Vowel Y Presence Confirmed: {str(y_vowel_state)}")
