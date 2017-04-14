import time

currentDate = (int)(time.strftime("%Y"))
age = (int)(input("Please input your current age: "))
print("You will be 100 in the year {0}".format((currentDate - age + 100)))
