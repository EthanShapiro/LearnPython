def getInteger():
    return int(input("Enter an integer:\n"))

def isPrimeNumber(dividend):
    divisors = range(2, 10)
    for divisor in divisors:
        if dividend % divisor == 0 and dividend != divisor:
            return False
    return True

number = getInteger()
print(isPrimeNumber(number))