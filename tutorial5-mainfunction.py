# main() example
import math


def rectangle_area():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    area = length * width

    print("The area of rect is:", area)


def circle_area():
    radius = float(input("Enter radius: "))
    area = math.pi * math.pow(radius, 2)

    print("The area of circle is: {:.2f}".format(area))


def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")


def main():
    shape_type = input("Get area for what shape: ")

    get_area(shape_type)


main()