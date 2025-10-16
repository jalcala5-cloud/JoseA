# Name: Joe Alcala
# Class: CIS188
# Lab 6 - String Processing Program
# Date: 10/10/2025

import random

# Function 1: Count characters (no spaces)
def count_characters(text):
    return len(text.replace(" ", ""))

# Function 2: Sixth character
def sixth_character(text):
    if len(text) >= 6:
        return text[5]
    else:
        return None

# Function 3: Uppercase version
def uppercase_text(text):
    return text.upper()

# Function 4: Repeat last word randomly
def repeat_last_word(text):
    words = text.split()
    if len(words) == 0:
        return ""
    last_word = words[-1]
    times = random.randint(3, 8)
    return (last_word + " ") * times

# Function 5: Word count dictionary
def word_count(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

# Function 6: Random 20-character slice
def random_slice(text):
    if len(text) < 20:
        return None
    start = random.randint(0, len(text) - 20)
    return text[start:start + 20]

# Main program
def main():
    print("Welcome to the 'Big Brother' String Processing Program!")
    print("Inspired by *1984* by George Orwell\n")
    print("Remember: Big Brother is watching you. 👁️‍🗨️\n")

    while True:
        text = input("Enter your favorite quote from 1984:\n")

        # 1. Count characters
        print("\nYour quote has", count_characters(text), "characters (no spaces).")

        # 2. Sixth character
        letter = sixth_character(text)
        if letter:
            print("The 6th character is:", letter)
        else:
            print("Your quote is too short to find the 6th character.")

        # 3. Uppercase version
        print("\nHere’s your quote in uppercase:")
        print(uppercase_text(text))

        # 4. Repeat last word
        print("\nRepeating the last word:")
        print(repeat_last_word(text))

        # 5. Word count
        print("\n-------- WORD COUNT --------")
        words = word_count(text)
        for word, count in words.items():
            print(f"{word:15} : {count}")

        # 6. Random 20-character slice
        print("\nRandom 20-character slice:")
        slice_text = random_slice(text)
        if slice_text:
            print(slice_text)
        else:
            print("Your quote is too short for a random slice.")

        # Ask to repeat
        again = input("\nDo you want to analyze another quote? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for sharing your favorite Orwell quote.")
            print("Remember: Big Brother is watching you. 👁️‍🗨️")
            break


# Run the program
main()
