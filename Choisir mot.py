import random

class Hangman():

    def __init__(self):
        self.possible_word = ['becode', 'learning', 'mathematics', 'sessions'] #liste de mot à trouver. 
        self.word_to_find = random.choice(self.possible_word) #utilisation du module random et de la fonction choice pour selectionner un mot au hasard dans la liste.
        self.word_to_find_list = list(self.word_to_find) # le module list pour séparer chaque caractère des mots.
        self.live = 8
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find) #len pour qu'il s'affice en "_" en fonction de la longueur du mot
        self.well_guessed_letters = []
        self.wrongly_guessed_letters = [] 
        self.turncount = 0
        self.error_count = 0

    def play(self):
        letter = input("Entrez une lettre : ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Erreur : Veuillez entrer une seule lettre.")
            return

        self.turn_count += 1
        if letter in self.word:
            self.guessed_letters.append(letter)
            print("Bien joué !")
            if self.is_word_guessed():
                self.well_played()
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1
            print("Raté ! Il vous reste {} vies.".format(self.lives))
            if self.lives == 0:
                self.game_over()

    def start_game(self):
        print("Le mot à deviner est : {}".format("_" * len(self.word)))
        while not self.is_game_over():
            self.play()
            print("Lettres bien devinées : {}".format(self.guessed_letters))
            print("Lettres mal devinées : {}".format(self.wrongly_guessed_letters))
            print("Vies restantes : {}".format(self.lives))
            print("Erreurs : {}".format(self.error_count))
            print("Nombre de tours : {}".format(self.turn_count))

    def game_over(self):
        print("Game over...")

    def well_played(self):
        print("Bravo ! Vous avez deviné le mot en {} tours avec {} erreurs.".format(self.turn_count, self.error_count))

    def is_game_over(self):
        return self.lives == 0 or self.is_word_guessed()

    def is_word_guessed(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True
