#!/usr/bin/python3

def loop(people, plants):
    weeks = 1
    fruits = 0
    plant = plants

    while fruits < people:
        weeks += 1
        fruits += plants
        plants += fruits

    return weeks


def main():
    print(loop(200, 15))
    print(loop(15, 1))
    print(loop(50000, 1))
    print(loop(150000,250))
main()
