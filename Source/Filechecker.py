def loadFile():
    isFile = False
    while (isFile == False):
        newfile = input("Enter a file please:")
        try:
            workFile = open(newfile)
            isFile = True
            for line in workFile:
                print(line)
            #return workFile
        except:
            isFile = False
            print("THAT IS NOT A FILE. PLEASE TRY AGAIN")

loadFile()
