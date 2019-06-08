class Game:
    word = ""
    currentWord = ""
    status = ""
    badGuess = 0
    missedLetters = 0
    actualMissedLetters = 0
    score = 0

    def __init__(self, word, status, badGuess, missedLetters, actualMissedLetters, score, currentWord):
        self.word = word
        self.status = status
        self.badGuess = badGuess
        self.missedLetters = missedLetters
        self.actualMissedLetters = self.actualMissedLetters
        self.score = score
        self.currentWord = currentWord
