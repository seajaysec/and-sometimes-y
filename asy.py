y_is_vowel = "UNKNOWN"
word_up = input("Enter your word: ").upper()
print(word_up)

if "Y" in word_up:
    print("Y found. Checking vowel status.")
    if {A, E, I, O, U} in word_up:
        print("Other vowels identified.")
    else:
        print("No other vowels identfied")
        y_is_vowel = "TRUE"
else:
    print("No Y found.")
