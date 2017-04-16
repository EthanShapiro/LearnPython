# How to use range
# range (start, end, step)
# range is inclusive, exclusive

# Loop from 0 to 9
startNum1 = 0
endNum1 = 10
for x in range(startNum1, endNum1):
    print (x)

# Loop from 0 to 20 by 5's
startNum2 = 0
endNum2 = 21
for x in range(startNum2, endNum2, 5):
    print (x)

# Loop from 10 to 1
startNum3 = 10
endNum3 = 0
for x in range(startNum3, endNum3, -1):
    print (x)

# How to use a while loop
# while x < 5 (conditional)

while x < 5:
    x += 1
    print(x)