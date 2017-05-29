nums = sorted([1, 50, 5, 3, 70, 23, 46, 22, 14, 12, 2])

def numInNumList(num):
    if num in nums:
        return True
    else:
        return False

print(numInNumList(1))
