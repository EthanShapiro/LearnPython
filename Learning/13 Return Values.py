# Return Values are something that a function can return to the caller (easier to see than to explain)
def allowedDatingAge(myAge):
    girlsAge = myAge/2 + 7
    return girlsAge

# Challenge at end of the video
ages = [14, 22, 57, 32, 29, 20]
for i in ages:
    print(allowedDatingAge(i))
