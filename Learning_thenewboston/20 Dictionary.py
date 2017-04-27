# Dictionaries in python (just like in real life) have a word and a definition
# But we call them key and value pairs instead
# Python dictionarys do not preserve order, meaning when they are printed, they will not be in any order
classmates = {'Tanner':'Funny and friendly', 'Karim':'Tall and can code', 'Chris':'Smart and plays baseball'}

print(classmates)
print(classmates['Tanner'])
print(classmates["Tanner"])

print("****************************")

for k, v in classmates.items():
    print(k,v)