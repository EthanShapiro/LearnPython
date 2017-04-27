myFile = open("myNewFile.txt", "w")  # Creates/Opens a file in write mode
myFile.write("This is the first line\nThe second line.\nThe third line.\n") # Write lines to a file using new lines
myLines = "this is a line", "this is also a line", "this also goes on a line"
myLines = "\n".join(myLines)
myFile.writelines(myLines)
myFile.close()

myFile = open("myNewFile.txt", "r") # Open the file in read mode
lines = myFile.readlines()  # get the lines from the file, and set them to a variable
print(type(lines))  # the lines from a file are lists of strings
for line in lines:print(line)  # loop through lines and perform operations on them

print("\n************************************\n")

# Use open with a to append, or add to the end of a file
with open("myNewFile.txt", "a") as f:  # Use open accompanied by with for automatic closing
    f.writelines("\nThis should be added when the file is in append mode")
with open("myNewFile.txt", "r") as f:
    print(f.read())

print("\n************************************\n")

# Use open with a+ to append and read
with open("myNewFile.txt", "a+") as f:
    print("\nFor a+ - ")
    print(f.readable())
    print(f.writable())

# Use open with r+ to read and write
with open("myNewFile.txt", "r+") as f:
    print("\nFor r+ - ")
    print(f.readable())
    print(f.writable())

# Use open with r+ to read and write
with open("myNewFile.txt", "w+") as f:
    print("\nFor w+ - ")
    print(f.readable())
    print(f.writable())
