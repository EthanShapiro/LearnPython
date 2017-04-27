# Dictionaries Definitions
myDict = {"One": 1, "Two": 2}
myDict1 = dict(One=1, Two=2)
myDict2 = dict(zip(['One', 'Two'], [1,2]))
myDict3 = dict({"One": 1, "Two": 2})

print(myDict.items())
print(myDict.keys())
print(myDict.values())

it = iter(myDict)
print(type(it))

for k in it: print(k) # If you loop through a dictionary it always prints the Keys

# To concatenate/Update a dictionary
newDict = {"One": 10, "Two": 2}
myDict.update(newDict)
print(newDict)

# You can also make a dictionary from a sequence
dictFromSeq = dict.fromkeys(["Seven", "Nine"])
print(dictFromSeq)
dictFromSeq1 = dict.fromkeys(["Seven", "Nine"], 10)
print(dictFromSeq1)