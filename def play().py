import random

def get_random_word():
    words = ['python', 'programmation', 'ordinateur', 'langage', 'algorithme', 'variable']
    return random.choice(words)

def play_hangman():
    MAX_TRIES = 6
    word = get_random_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    tries = 0

    while len(word_letters) > 0 and tries < MAX_TRIES:
        print(f"You have {MAX_TRIES - tries} tries left and you have used these letters: {' '.join(used_letters)}")

        # display the current status of the word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # get user input
        user_letter = input('Guess a letter: ').lower()

        # check if the user input is valid
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                tries += 1

        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")

        else:
            print("Invalid character. Please try again.")

    # the game is over at this point, display the result
    if tries == MAX_TRIES:
        print(f"Sorry, you lost! The word was {word}.")
    else:
        print(f"Congratulations! You guessed the word {word}!")
