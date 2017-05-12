import re
dotTest = 'a.s.d.a.s\n.d.as.'
print(re.findall('.', dotTest)) # Matches any character except a newline

caretTest = "abcdef"
print(re.search('$def', caretTest))
print(re.findall('[$\wa]', caretTest))

