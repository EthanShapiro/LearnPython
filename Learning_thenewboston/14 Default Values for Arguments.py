# variables in the () of the definition of a function are called arguments
# arguments are used to pass values to the function so it can perform it's intended, function
def setGender(sex="Unkown"):
    if sex is 'm':
        sex = "male"
    elif sex is 'f':
        sex = "female"
    else:
        sex = "Other"

print(setGender('m'))
print(setGender('f'))
print(setGender('banana'))