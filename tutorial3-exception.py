while True:

    try:
        number = int(input("please enter number: "))
        break

    except ValueError:
        print("You didn't enter a number")

    except:
        print("An unknown error occurred")

print("Thanks for entering a number!")
