f= open('file.txt', 'r')
lines = f.readlines()

newList = []
for line in lines:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)

print(newList)
