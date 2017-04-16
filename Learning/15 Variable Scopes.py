# Where a variable should be defined depending on what things use it

a = 8239

def corn():
    print(a)

def beef():
    print(a)

def watermelon():
    b = 18834
    print(b)

corn()
beef()
watermelon()