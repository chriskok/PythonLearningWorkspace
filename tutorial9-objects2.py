class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("retrieving height")

        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    @property
    def width(self):
        print("retrieving width")

        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def getArea(self):
        return int(self.__width) * int(self.__height)


def main():
    aSqaure = Square()

    # print(aSqaure.height)

    height = input("Enter height: ")
    width = input("Enter width: ")

    aSqaure.height = height
    aSqaure.width = width

    print("H:", aSqaure.height)
    print("W:", aSqaure.width)
    print("A:", aSqaure.getArea())

main()