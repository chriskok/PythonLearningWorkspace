import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more!")

with open("mydata.txt", encoding="utf-8") as myFile:
    lineNum = 1

    while True:
        line = myFile.readline()

        if not line:
            break

        # print("line #", lineNum, ":", line, end="")
        # split()
        wordList = line.split()

        # len() <- words in a line
        print("words:", len(wordList))

        # loop and count each of the characters in the list
        cCount = 0
        for word in wordList:
            for char in word:
                cCount += 1

        # calculate the avg (char count / len word)
        avg = cCount/len(wordList)

        print("Average word length: {:.2}".format(avg))

        lineNum += 1