def loadFile():
    isFile = False
    while (isFile == False):
        newfile = input("Enter a file please:")
        try:
            workFile = open(newfile)
            isFile = True
        except:
            isFile = False
            print("THAT IS NOT A FILE. PLEASE TRY AGAIN")

loadFile()
