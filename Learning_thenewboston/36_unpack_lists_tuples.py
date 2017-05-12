fruit, screen, dollar = ["banana", "monitor", 8.15] # You can unpack lists into individual variables
print(fruit, screen, dollar)

def dropFirstLast(grades):
    grades = sorted(grades)
    first, *middle, last = grades  # unpack grades and take first and last numbers, and put all the numbers in the
    avg = sum(middle) / len(middle) # get average of all grades
    print(avg)

dropFirstLast([1, 10, 30, 20])