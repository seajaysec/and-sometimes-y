#!/usr/bin/env python3 -tt
# Chris Farrell - @seajay - https://github.com/seajaysec/
"""
Identifies whether Y is a consonant or vowel in a given word.
"""
y_vowel_state = "UNKNOWN"
static_vowels = ["A", "E", "I", "O", "U"]
word_up = input("Enter your word: ").upper()
print(word_up)

if "Y" in word_up:
    print("Y found. Checking vowel status.")
    static_vowel_match = [chars in static_vowels for chars in word_up]
    other_vowel_present = any(static_vowel_match)
    if other_vowel_present == "True":
        print("Other vowels identified.")
    else:
        print("No other vowels identfied")
        y_vowel_state = "True"
else:
    print("No Y found.")
    y_vowel_state = "NOT POSSIBLE"

print("Vowel Y Presence is: " + y_vowel_state)
