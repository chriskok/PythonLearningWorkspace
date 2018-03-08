class Animal:
    def __init__(self, birthType="Unknown", appearance="Unknown",
                 blooded="Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__,
                                                     self.birthType,
                                                     self.appearance, self.blooded)


class Mammal(Animal):
    def __init__(self, birthType="born alive",
                 appearance="hair or fur", blooded="warm blooded", nurseYoung=True):
        Animal.__init__(self, birthType, appearance, blooded)
        self.nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # MAGIC METHOD
    def __str__(self):
        return super().__str__() + " and it is {} they nurse" \
                                   "their young".format(self.nurseYoung)


class Reptile(Animal):
    def __init__(self, birthType="born in egg or alive",
                 appearance="dry scales", blooded="cold blooded"):
        Animal.__init__(self, birthType, appearance, blooded)

    def sumAll(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum


def getBirthType(theObject):
    print("The {} is {}".format(type(theObject).__name__,
                                theObject.birthType))


def main():
    animal1 = Animal("born alive")
    print(animal1.__str__())
    print(animal1)  # same thing as above

    mammal1 = Mammal()
    print(mammal1.__str__())

    reptile1 = Reptile()
    print(reptile1.birthType)
    print(reptile1.appearance)
    print(reptile1.blooded)
    print(reptile1)
    print("Sum: {}".format(reptile1.sumAll(1, 2, 3, 4, 5)))

    getBirthType(mammal1)
    getBirthType(reptile1)


main()
