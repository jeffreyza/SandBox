'''
Author: Bozo the Clown
Date: 30 Jul 2021
Description:
Demo of pycharm with Git and Github
'''

from utilities import *


def main():
    print("Hello, My name is Bozo")
    for i in range(1, 6):
        print_stars(i)

    print("area of circle with radius of 5 units: {:.2f}\n".format(calculate_area_of_circle(5)))


def print_stars(number):
    print("*" * number)


if __name__ == '__main__':
    main()
