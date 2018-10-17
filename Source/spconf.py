isFile = False
while (isFile == False):
    newfile = input("Enter a file please:")
    try:
        workFile = open(newfile)
        isFile = True
    except:
        isFile = False
        print("THAT IS NOT A FILE. PLEASE TRY AGAIN")

count = 0
spamSum = 0
hiCount = 0
for line in workFile:        
    spam = line

    perc = spam.split(' ', 1)[1]
    perc = float(perc)
    spamSum += perc
    count = count + 1
    if perc > .90:
        hiCount = hiCount + 1

totPerc = spamSum/count
        

print("The average spam confidece is:" , totPerc)
print("The number of emails above 90% spam is:" , hiCount)
