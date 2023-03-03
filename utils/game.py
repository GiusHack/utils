import random

class Hangman():

    def __init__(self):
        self.possible_word = ['becode', 'learning', 'mathematics', 'sessions'] #liste de mot à trouver. 
        self.word_to_find = random.choice(self.possible_word) #utilisation du module random et de la fonction choice pour selectionner un mot au hasard dans la liste.
        self.word_to_find_list = list(self.word_to_find) # le module list pour séparer chaque caractère des mots.
        self.live = 5
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find) #len pour qu'il s'affice en "_" en fonction de la longueur du mot
        self.well_guessed_letters = []  #Pour dire que c'est une liste
        self.wrongly_guessed_letters = [] 
        self.turncount = 0 # depart 0 et indique que c'est un nombre
        self.error_count = 0
        
    def play(self):
        while True:
            in_put = input("Enter a letter: ").lower()
            if len(in_put) != 1: # condition de si l'input est pas égale a 1 ca renvoi "plaese enter a signle letter"
                print("Please enter a single letter.")
            elif not in_put.isalpha(): #isalpha() renvoie: true Si tous les caractères de la chaîne sont des lettre et fasle si autre.
                print("Please enter a letter.")
            else:
                break

        self.turncount += 1 # Pour augmenter de 1 le nombre d'essaye a chaque tour
        if in_put in self.word_to_find:
            for i, letter in enumerate(self.word_to_find): # j'utilise la fonction enumerate afin de remplacer l'underscore par la lettre trouvée
                if letter == in_put: #condition pour que l'input soit egale a la lettre a trouver
                    self.correctly_guessed_letters[i] = letter # ajout de la bonne lettre au bon endroit à la liste correctly letter

        else:
            self.wrongly_guessed_letters.append(in_put) # rajouter l'input dans la liste self.wrongle_guessed_letters
            self.error_count += 1 # ajouter une erreur
            self.live -= 1 # enlever une vie

    
    def well_played(self):
        print("You found the word: {}".format(self.word_to_find), "in {}".format(self.turncount), "turns with {}".format(self.error_count), "errors!.")
   
    def game_over(self): 
        print("Game over. The word was: ", self.word_to_find)
    """
    les deux fonctions si dessus permettre l'affichage de la victoire ou de la defaite, 
    on les implémantera dans la fonction "start_game".
    """

    def start_game(self): 
        while self.live > 0: #condition de fonctionnement qui dit que la boucle continue tant self.live est plus grans que 0
            self.play() # Rappelle de la fonction self.play pour que le jeu commence
            print(" ".join(self.correctly_guessed_letters)) #affichage de la bonne lettre au lieu du underscore
            print(" ".join(self.wrongly_guessed_letters)) # rajout de la mauvaise lettre dans la liste self_wrongly_guesse_letters
            if "_" not in self.correctly_guessed_letters : #condition de si il y a plus d'underscore dans self.correctly_guessed_letters afficher well played
                self.well_played()
                return # Arret de la boucle
        if self.live == 0: # condition si il y a plus de viec ca va afficher game_over()
            self.game_over()
            return # Arret de la boucle
        

