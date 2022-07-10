import numpy as np


def print_neighbour(hood, i_row, i_elem, side):
    if side == 'top':
        print("Top neighbour is: ", hood[i_row - 1][i_elem])
    elif side == 'bottom':
        print("Bottom neighbour is: ", hood[i_row + 1][i_elem])
    elif side == 'left':
        print("Left neighbour is: ", hood[i_row][i_elem - 1])
    elif side == 'left-top-d':
        print("Left-top-diagonal neighbour is: ", hood[i_row - 1][i_elem - 1])
    elif side == 'right-top-d':
        print("Right-top-diagonal neighbour is: ", hood[i_row - 1][i_elem + 1])
    elif side == 'left-bottom-d':
        print("Left-bottom-diagonal neighbour is: ", hood[i_row + 1][i_elem - 1])
    elif side == 'right-bottom-d':
        print("Right-bottom-diagonal neighbour is: ", hood[i_row + 1][i_elem + 1])
    else:
        print("Right neighbour is: ", hood[i_row][i_elem + 1])


hood = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

num = 22
for i_row in range(0, len(hood)):
    for i_elem in range(0, len(hood[i_row])):
        if hood[i_row][i_elem] == num:

            top_okay = i_row >= 1
            bottom_okay = i_row < len(hood) - 1
            left_okay = i_elem >= 1
            right_okay = i_elem < len(hood[i_row]) - 1

            if top_okay:
                print_neighbour(hood, i_row, i_elem, "top")
            if bottom_okay:
                print_neighbour(hood, i_row, i_elem, "bottom")
            if left_okay:
                print_neighbour(hood, i_row, i_elem, "left")
            if right_okay:
                print_neighbour(hood, i_row, i_elem, "right")
            if top_okay and left_okay:
                print_neighbour(hood, i_row, i_elem, "left-top-d")
            if top_okay and right_okay:
                print_neighbour(hood, i_row, i_elem, "right-top-d")
            if bottom_okay and left_okay:
                print_neighbour(hood, i_row, i_elem, "left-bottom-d")
            if bottom_okay and right_okay:
                print_neighbour(hood, i_row, i_elem, "right-bottom-d")
