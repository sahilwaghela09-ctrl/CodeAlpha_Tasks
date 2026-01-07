import random

# Predefined list of words
words = ["python", "coding", "hangman", "simple", "logic"]

# Randomly choose a word
word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while attempts > 0:
    # Display current word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Attempts left:", attempts)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        print("Good guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        attempts -= 1

# If attempts are exhausted
if attempts == 0:
    print("\nGame Over! The word was:", word)
