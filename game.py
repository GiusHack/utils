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
        
    """
    def display(self):
        for l in range(len(self.word_to_find)):
            self.word_to_find[l] = "-" * len(self.word_to_find[l])
            print(self.word_to_find)
            #fonction faite avant de comprendre que je pouvais le faire dans l'init
    

    def play(self):
        letter = input("Guess a letter: ")
        if letter == self.correctly_guessed_letters:
"""
    def play(self):
        letter = input("Enter a letter : ")
        self.turncount += 1
        if letter in self.word_to_find:
            self.well_guessed_letters += [letter]
        else:
            self.wrongly_guessed_letters += [letter]
        self.error_count += 1

    def start_game(self):
        while self.live > 0:
            def play(self):
            
                if self.live == 0:
                    print("game over")
                else:
                    print("well game")

hangman = Hangman()



