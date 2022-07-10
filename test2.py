from math import pi


def ellipse_area(major, minor):
    return pi * major * minor

def rectangle_area(base, height):
    return base * height

def trapezoid_area(top, bottom, height):
    return 0.5 *  height * (top + bottom)


def is_valid_shape(in_value):
    if in_value == 'ellipse' or in_value == 'trapezoid' or in_value == 'rectangle' or in_value == 'done':
        return True
    else:
        return False


def main():
    area_list = list()

    in_value = input('What shape would you like to calculate?\n')
    in_value = in_value.lower()
    is_valid_shape(in_value)

    while is_valid_shape(in_value) == True:
        if in_value == "ellipse":
            major = float(input('What is the major radius of the ellipse?\n'))
            minor = float(input('What is the minor radius of the ellipse?\n'))
            print(f"The calculated area is", round(ellipse_area(major, minor), 2))
            area_list.append(ellipse_area(major, minor), 2)

        if in_value == "rectangle":
            base = float(input("What is the length of the rectangle's base?\n"))
            height = float(input("What is the height of the rectangle?\n"))
            print(f"The calculated area is", round(rectangle_area(base, height), 2))
            area_list.append(round(rectangle_area(base, height), 2))

        if in_value == "trapezoid":
            top = float(input("What is the length of the trapezoid's top?\n"))
            bottom = float(input("What is the length of the trapezoid's bottom?\n"))
            height = float(input("What is the trapezoid's height?\n"))
            print(f"The calculated area is", round(trapezoid_area(top, bottom, height), 2))
            area_list.append(round(trapezoid_area(top, bottom, height), 2))

        else:
            print("Thanks for using this program! Here is a list of the areas that we calculated for you:")

        in_value = ('What shape would you like to calculate\n')

        if in_value != "done":
            print("Sorry, but that shape doesn't exist in our system. Please try again.")
        else:
            print("Thanks for using this program! Here is a list of the areas that we calculated for you:")


if __name__ == "__main__":
    main()

