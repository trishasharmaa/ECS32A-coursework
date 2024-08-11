def display_hangman(incorrect_guesses):
    hangman_parts = [
        "  |",
        "  0",
        " /",
        ]
    print("Hangman:")
    print("".join(hangman_parts[:incorrect_guesses]))

def get_valid_secret_word():
    while True:
        secret_word = input("Please enter a word to be guessed "
                            "that does not contain ? or whitespace: ").strip().lower()
        if secret_word and '?' not in secret_word and ' ' not in secret_word:
            return secret_word
        else:
            print("Invalid input. Please enter a valid word.")
def display_word(secret_word, guessed_letters):
    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "?"
    return displayed_word

def get_valid_guess(guessed_letters: set) -> str:
    while True:
        guess = input("Please enter your next guess: ").strip().lower()
        if guess and len(guess) == 1 and guess not in guessed_letters:
            return guess
        elif guess in guessed_letters:
            print("You already guessed the character:", guess)
        else:
            print("You can only guess a single character.")

def display_guessed_letters(guessed_letters):
    sorted_letters = sorted(guessed_letters)
    print("So far you have guessed:", ", ".join(sorted_letters))

def main():
    secret_word = get_valid_secret_word()
    guessed_letters = set()
    incorrect_guesses = 0

    while incorrect_guesses < len(guessed_letters):
        display_hangman(incorrect_guesses)
        displayed_word = display_word(secret_word, guessed_letters)
        print("Current word:", displayed_word)
        display_guessed_letters(guessed_letters)

        if displayed_word == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess not in secret_word:
            incorrect_guesses += 1

    if incorrect_guesses == len(hangman_parts):
        print("Hangman complete. You didn't guess the word. The word was:", secret_word)

if __name__ == "__main__":
    main()








