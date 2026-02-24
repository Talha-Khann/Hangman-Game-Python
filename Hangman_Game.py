import random

# small predefined list (as required)
WORDS = ["python", "intern", "hangman", "developer", "keyboard"]

def choose_word():
    # using random module
    return random.choice(WORDS)  

def show_progress(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    word = choose_word()
    guessed_letters = []
    wrong_attempts = 0
    # limit incorrect guesses to 6
    max_attempts = 6  

    print("\n=== HANGMAN GAME ===")
    print("Guess the word one letter at a time.\n")

    # while loop for game running
    while wrong_attempts < max_attempts:

        print("Word:", show_progress(word, guessed_letters))
        print("Attempts left:", max_attempts - wrong_attempts)
        
        # console input
        guess = input("Enter a letter: ").lower().strip()  

        # basic validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter single letter.\n")
            continue

        if guess in guessed_letters:
            print("Already guessed.\n")
            continue

        guessed_letters.append(guess)

        # if-else logic for checking guess
        if guess in word:
            print("Correct!\n")
        else:
            wrong_attempts += 1
            print("Wrong!\n")

        # win condition
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You won 🎉")
            print("Word was:", word)
            return

    print("Game Over! You lost ❌")
    print("Word was:", word)

if __name__ == "__main__":
    main()