def countWordsFromFile():
    fileName=input('Name of the file: ')
    numberOfWords=0
    f=open(fileName, "r")
    for i in f:
        words=i.split()
        numberOfWords=numberOfWords+len(words)
    print("Number of words: " + str(numberOfWords))

countWordsFromFile()