import os
import random

WORDS_FILE = f"{os.path.dirname(__file__)}/resources/words_alpha.txt"

def get_random_word():
    with open(WORDS_FILE, 'r') as f:
        line = next(f)
        for num, l in enumerate(f, 2):
            if random.randrange(num):
                continue
            line = l
        return line

def get_rhyming_word(word, accuracy = 1.0):
    pass