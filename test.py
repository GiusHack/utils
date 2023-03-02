lettres = ['boujour', 'bijour', 'coucou']

for position, lettre in enumerate(lettres):
  print(position, lettre)

import random

possible_word = list(random.choice(['becode', 'learning', 'mathematics', 'sessions']))
word_to_find = list("_" * len(possible_word))

for position, letter in enumerate(word_to_find):
  print(position, letter)

