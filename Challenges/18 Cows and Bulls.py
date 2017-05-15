import random

if __name__=="__main__":
    randNum = str(random.randint(1000, 9999))
    numCows = 0
    numBulls = 0
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
        x = 0
        while x < len(randNum):
            if(randNum[x] == playerGuess[x]):

            x += 1


