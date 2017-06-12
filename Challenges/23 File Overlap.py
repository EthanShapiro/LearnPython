f1 = open("file1.txt", 'r')
f2 = open("file2.txt", 'r')

lines1 = f1.readlines()
lines2 = f2.readlines()
lines1 = [line.strip() for line in lines1]
lines2 = [line.strip() for line in lines2]

overlapNums = list(set(lines1).intersection(set(lines2)))
overlapNums = [int(num) for num in overlapNums]
print(sorted(overlapNums))
