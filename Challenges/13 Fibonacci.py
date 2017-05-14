def getFibonacciSequence(nums):
    num = 0
    a = [1]
    while num < nums:
        if (len(a) > 1):
            a.append(a[len(a)-1] + a[len(a)-2])
        else:
             a.append(a[0])
        num +=1
    return a

print(getFibonacciSequence(8))