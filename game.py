import random

words = ['becode', 'learning', 'mathematics', 'sessions']
def random_word():
    words = ['becode', 'learning', 'mathematics', 'sessions']
def random_word():
    word = random.choice(words)
    return word
random_word()

""""
le module random génere des nombres ou des mots de manière aléatoire,
dans notre cas nous utilisont random + la fonction choise pour piocher
de manière aléatoire dans la liste "possible_word".

"""

def display(words, good_letters):
    displayed_word = ""
    for l in words: 
        if l in good_letters:
            displayed_word += l
        else:
            displayed_word += "-"
        return displayed_word
display()
     
