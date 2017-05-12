# Class variables are associated with every object Girl
# Instance variables are associated with their specific object
class Girl:

    gender = "female" # This is a class variable that every girl will have

    def __init__(self, name):
        self.name = name # this is an instance variable

r = Girl("Rachel")
s = Girl("Sarah")
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)