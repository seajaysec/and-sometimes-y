y_vowel_state = "UNKNOWN"
static_vowels = ["A", "E", "I", "O", "U"]
word_up = input("Enter your word: ").upper()
print(word_up)

if "Y" in word_up:
    print("Y found. Checking vowel status.")
    if ["A", "E", "I", "O", "U"] in word_up:
        print("Other vowels identified.")
    else:
        print("No other vowels identfied")
        y_vowel_state = "TRUE"
else:
    print("No Y found.")
    y_vowel_state = "NOT POSSIBLE"

print(f"Y vowel state is {y_vowel_state}")
