class Enemy:
    def __init__(self, health):
        self.health = health

    def getHealth(self):
        print(self.health)

enemy1 = Enemy(10)
enemy1.getHealth()