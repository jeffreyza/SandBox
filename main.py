'''
Author: Bozo the Clown
Date: 30 Jul 2021
Description:
Demo of pycharm with Git and Github
'''


def main():
    print("Hello, My name is Bozo")
    for i in range(1, 6):
        print_stars(i)

def print_stars(number):
    print("*" * number)


if __name__ == '__main__':
    main()