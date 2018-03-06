'''
Sam attacks Paul and deals 9 dmg
Paul is down to 10 health
Paul attacks Sam and deals 7 dmg
Sam is down to 7 health
Same attacks Paul and deals 19 damage
Paul is down to -9 health
Paul died
Game Over
'''


import random


class Warrior:
    def __init__(self, name="Warrior", health="30"):
        self.name = name
        self.health = health

    @property
    def health(self):
        # print("retrieving health")

        return self.__health

    @health.setter
    def health(self, value):
        if value.isdigit():
            self.__health = value
        else:
            print("Please only enter numbers for height")

    def deducthealth(self, value):
        self.__health = str(int(self.__health) - value)
        return int(self.__health)


def main():
    sam = Warrior("Sam", "50")
    paul = Warrior("Paul", "70")

    while True:
        dmg = random.randint(0,40)
        print('{} attacks {} and deals {} damage'.format(sam.name, paul.name, dmg))
        print('{} is down to {} health'.format(paul.name, paul.deducthealth(dmg)))

        if int(paul.health) <= 0:
            print('{} has died, {} is victorious'.format(paul.name, sam.name))
            break

        dmg = random.randint(0,40)
        print('{} attacks {} and deals {} damage'.format(paul.name, sam.name, dmg))
        print('{} is down to {} health'.format(sam.name, sam.deducthealth(dmg)))

        if int(sam.health) <= 0:
            print('{} has died, {} is victorious'.format(sam.name, paul.name))
            break


main()

