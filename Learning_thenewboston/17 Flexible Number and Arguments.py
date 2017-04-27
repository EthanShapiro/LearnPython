def addNumbers(*args):
    total = 0
    for a in args:
        total += a
    return total

print(addNumbers(5, 1, 5, 6, 7, 89, 10))
print(addNumbers())