import random

if __name__=="__main__":
    randNum = str(random.randint(1000, 9999))
    numCowsAndBulls = [0, 0]
    numGuesses = 0
    def getPlayerGuess():
        playerGuess = None
        while True:
            try:
                playerGuess = input("Please enter a 4 digit number, and we'll tell you how many cows and bulls you have")
                if playerGuess > 9999 or playerGuess < 1000:
                    continue
            except ValueError:
                continue
            else:
                break
        return playerGuess

    playerGuess = getPlayerGuess()
    def checkPlayerGuess(playerGuess):
        if playerGuess == randNum:
            print("You guessed the number {0} in {1} guesses!".format(randNum, numGuesses))

    def checkNumCows(playerGuess):

    def checkNumBulls(playerGuess):



