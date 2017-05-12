# Inheritance is like acquiring everything from the class inhereted from
class Parent():

    def printLastName(self):
        print('Shapiro')

class Child(Parent):  #this is how you inheritance from a class

    def printFirstName(self): # Classes that inherit another class can have their own functions
        print('Ethan')

    def printLastName(self): # You can also override functions inherited
        print("BananaCake")

c = Child()
c.printFirstName()
c.printLastName()