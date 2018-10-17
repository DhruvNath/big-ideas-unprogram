def loadFile():
    isFile = False
    while (isFile == False):
        newfile = input("Enter a file please:")
        try:
            workFile = open(newfile)
            isFile = True
            return workFile
        except:
            isFile = False
            print("THAT IS NOT A FILE. PLEASE TRY AGAIN")

workFile = loadFile()
allWords = []
for line in workFile:
    line = line.lower()
    line = line.split('\n')[0]
    lineCheck = line.split(' ')
    for word in lineCheck:
        if word not in allWords:
            allWords.append(word)
            
allWords.sort()
print(allWords)
