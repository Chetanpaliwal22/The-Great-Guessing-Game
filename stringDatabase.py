import random


class StringDatabase:
    words = []

    thisdict = {
        '-': 0,
        'a': 8.17,
        'b': 1.49,
        'c': 2.78,
        'd': 4.25,
        'e': 12.70,
        'f': 2.23,
        'g': 2.02,
        'h': 6.09,
        'i': 6.97,
        'j': 0.15,
        'k': 0.77,
        'l': 4.03,
        'm': 2.41,
        'n': 6.75,
        'o': 7.51,
        'p': 1.93,
        'q': 0.10,
        'r': 5.99,
        's': 6.33,
        't': 9.06,
        'u': 2.76,
        'v': 0.98,
        'w': 2.36,
        'x': 0.15,
        'y': 1.97,
        'z': 0.07
    }

    def readFile(self):
        '''Method to read file'''
        file = open("four_letters.txt", "r")
        contents = file.read()
        self.words = contents.split()
        return self.words

    def generateRandomWord(self, words):
        '''Method to generate the random word'''
        return random.choice(words)
