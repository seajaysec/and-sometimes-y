y_vowel_state = "UNKNOWN"
static_vowels = ["A", "E", "I", "O", "U"]
word_up = input("Enter your word: ").upper()
print(word_up)

if "Y" in word_up:
    print("Y found. Checking vowel status.")
    static_vowel_match = [chars in static_vowels for chars in word_up]
    if any(static_vowel_match) == "TRUE":
        print("Other vowels identified.")
    else:
        print("No other vowels identfied")
        y_vowel_state = "TRUE"
else:
    print("No Y found.")
    y_vowel_state = "NOT POSSIBLE"

print("Y vowel state is {y_vowel_state}")
