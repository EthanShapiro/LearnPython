class Enemy:
    life = 3

    def takeDamage(self):
        print("ouch!")
        self.life -=1

    def checkLife(self):
        if self.life <= 0:
            print("I'm Dead!")
        else:
            print(str(self.life), "life left")

enemy1 = Enemy()
enemy1.takeDamage()
enemy1.checkLife()

enemy2 = Enemy()
enemy2.checkLife()