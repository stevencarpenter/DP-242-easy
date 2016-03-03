#!/usr/bin/python

import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("people", help = "number of people to be supported", type = int)
    parser.add_argument("fruits", help = "number of fruits to start", type = int)
    args = parser.parse_args()

    print(args.people)
    print(args.fruits)


main()
