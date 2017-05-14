import string
import random
def getPassword(length):
    x = 0
    allChars = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    password = []

    while x < length:
        charType = allChars[random.randint(0, len(allChars)-1)]
        password.append(charType[random.randint(0, len(charType)-1)])
        x += 1
    return "".join(password)

print(getPassword(8))
