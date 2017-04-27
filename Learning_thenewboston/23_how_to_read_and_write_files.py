fw = open("sample.txt", 'w')
fw.write("this is some new stuff.\nThis is for a different line.")
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
