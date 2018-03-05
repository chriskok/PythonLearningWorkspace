import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more!")

# Read by default
with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())  # either read(), readline(), readlines()

print(myFile.closed)

print(myFile.name)

print(myFile.mode)

os.rename("mydata.txt", "mydata2.txt")

os.remove("mydata2.txt")

os.mkdir("mydir")

os.chdir("mydir")

print("Current dir:", os.getcwd())

os.chdir("..")

os.rmdir("mydir")