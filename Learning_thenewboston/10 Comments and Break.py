# This is a comment
# Comments are used to help explain the logic behind the code, not the code itself
# Bad code should not be explained with comments, instead rewrite the code to be

magicNumber = 4

# Search for the magic number
for i in range(101):
    if i == magicNumber:
        print("Found magic number")
        break

while True:
    print("This is before the break")
    break
