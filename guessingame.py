# Create do while loop to allow users to keep guessing a random number from 1 to 10
import random
rand_num = random.randrange(1, 11)

print("cheat: ", rand_num)

# Do while loop
while True:
    try:
        guess = int(input("Enter a guess: "))
        if guess == rand_num:
            print("YOU GOT IT!")
            break

    except ValueError:
        print("Please enter a number!")

    except:
        print("An unknown errpr occurred")

