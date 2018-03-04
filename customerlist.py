# array of cust dictionaries
# Enter cust (y/n)
# Enter cust name: Derek
# repeat till n received
# Derek Banas
# Sally Smith

choice = input("Enter customer name? (yes/no): ")
custList = []

while choice == 'y' or choice == 'yes':
    fName, lName = input("Please enter customer's name: ").split()
    custList.append({'fName': fName, 'lName': lName})
    choice = input("Enter customer name? (yes/no): ")
    while choice != 'y' and choice != 'yes' and choice != 'n' and choice != 'no':
        choice = input("Invalid input, please enter again: ")

for i in custList:
    print(i['fName'], i['lName'])
