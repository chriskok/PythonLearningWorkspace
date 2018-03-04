# Dictionaries are similar to lists, or Hashmaps in Java

chrisDict = {"fName": "Chris", "lName": "Kok", "addr": "123 Main St"}

print("My Name:", chrisDict["fName"])

chrisDict["addr"] = "215 North St"

print(chrisDict) # Non sequential

chrisDict['city'] = 'Pittsburgh'

print("city" in chrisDict)

print(chrisDict.values())

print(chrisDict.keys())

for k, v in chrisDict.items():
    print(k,v)

print(chrisDict.get("mName", "Not Here"))

del chrisDict['fName']

for i in chrisDict:
    print(i)

chrisDict.clear()

employees = []

fName, lName = input("Enter Employee Name: ").split()

employees.append({'fName': fName, 'lName': lName})

print(employees)