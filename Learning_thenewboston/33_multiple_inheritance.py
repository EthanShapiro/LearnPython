class Mario():

    def move(self):
        print("I am moving")

class Mushroom():

    def eatMushroom(self):
        print("Now I am big")

class BigMario(Mario, Mushroom):
    pass

bM = BigMario()
bM.eatMushroom()
bM.move()