from stringDatabase import StringDatabase
from game import Game


class Guess:

    word = ""
    gameArray = []
    gameList = list()

    def __init__(self):
        self.guessWord = "----"

    def main(self):
        text = "a"
        exitFlag = True
        guess.word = objStringDatabase.generateRandomWord(wordArray).lower()
        self.word = guess.word
        self.guessWord = "----"
        game = Game(self.word, "", 0, 0, 0, 0, "----")
        while text != "q" or text != "Q":
            #print("Your word is: "+self.word)
            print(
                "-------------------------------------------------------------------------------------------------")
            print("** The great guessing game **")
            print("Current Guess: "+game.currentWord)
            print()
            text = input(
                "g = guess, t = tell me, l for a letter, and q to quit:  ").lower()
            print
            if text == "g":
                exitFlag = False
                guessWord = input(
                    "Okay Sir, Here you go make the wild guess:  ").lower()
                checkFlag = self.guessWordMethod(guessWord, game)
                if checkFlag:
                    self.calculateScore(game)
                    guess.word = objStringDatabase.generateRandomWord(
                        wordArray).lower()
                    self.word = guess.word
                    self.guessWord = "----"
                    game = Game(self.word, "", 0, 0, 0, 0, "----")
                    exitFlag = True
                    # break
            elif text == "t":
                self.tellWord(game)
                self.calculateScore(game)
                guess.word = objStringDatabase.generateRandomWord(
                    wordArray).lower()
                self.word = guess.word
                self.guessWord = "----"
                game = Game(self.word, "", 0, 0, 0, 0, "----")
                exitFlag = True
                # break
            elif text == "l":
                exitFlag = False
                self.guessLetter(game)
                if guess.guessWord.count('-') == 0:
                    game.status = "Success"
                    self.calculateScore(game)
                    exitFlag = True
                    # break
                    guess.word = objStringDatabase.generateRandomWord(
                        wordArray).lower()
                    self.word = guess.word
                    self.guessWord = "----"
                    game = Game(self.word, "", 0, 0, 0, 0, "----")

            elif (text == "q" or text == "Q"):
                game.status = "Gave up"
                if exitFlag:
                    game = Game(self.word, "", 0, 0, 0, 0, "----")
                    self.displayFinalScore(game)
                    break
                else:
                    self.calculateScore(game)
                    exitFlag = True
                    self.word = objStringDatabase.generateRandomWord(
                        wordArray).lower()
                    game = Game(self.word, "", 0, 0, 0, 0, "----")
                    self.displayFinalScore(game)
                    break

            else:
                print("Sir, Please follow the correct choice ...")

    def guessWordMethod(self, text, game):
        '''Method to handle the Guess word scenario'''
        if self.word == text:
            print("Correct Guess. You are genious!")
            game.status = "Success"
            return True
        else:
            print("That was a bad guess... Please try again")
            game.badGuess = game.badGuess + 1
        return False

    def tellWord(self, game):
        '''Method to handle the gave up scenario'''
        game.status = "Gave up"
        print("Ah!! The word was : "+self.word)
        print("Try fresh with this new word ... ")

    def guessLetter(self, game):
        '''Method to handle the Guess Letter scenario'''
        text = input(
            "Here you go.... Guess a letter:  ").lower()
        if(len(text) == 1):
            origWord = list(self.word)
            # guessWord = list(text)
            currentWord = list(guess.guessWord)
            i = 0
            correctGuess = 0
            for char in origWord:
                if origWord[i] == text:
                    correctGuess = correctGuess + 1
                    currentWord[i] = text
                i = i+1

            guess.guessWord = str("".join(currentWord))
            game.currentWord = guess.guessWord
            game.missedLetters = game.missedLetters + 1
            if(correctGuess == 0):
                game.actualMissedLetters = game.actualMissedLetters + 1
                print(
                    "Sorry... You were not able to guess any character ... Try again !")
            if correctGuess > 0:
                print("Great you were abppydocle to guess " +
                      str(correctGuess) + " characters! Continue the game")
            print("Your string after guessing: "+game.currentWord)
        else:
            game.actualMissedLetters = game.actualMissedLetters + 1
            game.missedLetters = game.missedLetters + 1
            print(
                "Sir!!! You are asked to guess a letter not a word or empty string... Please try again.")

    def displayFinalScore(self, game):
        '''Method to display the final score'''
        finalScore = 0
        srNumber = 1
        printFlag = False
        for game in self.gameList:
            printFlag = True
            if srNumber == 1:
                print("Game    " + "Word    " + "Status    " +
                      "Bad Guesses    " + "Missed Letters    " + "Score    ")
                print("----    ----    ------    -----------    --------------    -----")

            print(str(srNumber)+"   " + "    " + game.word + "    " + game.status+"        " +
                  str(game.badGuess) + "              "+str(game.actualMissedLetters) + "            " + str(game.score))
            srNumber = srNumber+1
            finalScore = finalScore + game.score

        if printFlag:
            print("----------------------------------------------------------------")

            print("Thank you for Playing !!!")
            print("Final Score: "+str(finalScore))

    def calculateScore(self, game):
        '''Method to calculate score'''
        scoreTotalWord = self.calculateStringScore(game.word)
        scoreUnCoveredChar = self.calculateStringScore(game.currentWord)
        if(game.status == "Gave up"):
            finalScore = (scoreTotalWord - scoreUnCoveredChar)*-1
            game.score = finalScore
        if(game.status == "Success"):
            scoreInterm = scoreTotalWord - scoreUnCoveredChar
            if(game.missedLetters > 0):
                scoreInterm = scoreInterm/(game.missedLetters)
            n = game.badGuess
            for i in range(n):
                scoreInterm = scoreInterm - scoreInterm * 0.1
            game.score = scoreInterm
        self.gameList.append(game)
        # print("score of the string is: "+str(game.score))

    def calculateStringScore(self, localWord):
        '''Method to calculate score of the string'''
        dict = StringDatabase.thisdict
        scoreLocal = 0
        for char in localWord:
            scoreLocal = scoreLocal + dict[char]
        return scoreLocal


guess = Guess()
objStringDatabase = StringDatabase()
wordArray = objStringDatabase.readFile()
guess.main()
