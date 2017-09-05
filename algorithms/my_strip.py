#!/bin/python3

import sys

def my_strip(string):
    j, i = 0, 0
    l = len(string)
    for p in range(l):
        if string[p] != ' ':
            string = string[p-1:]

    return string


string = input()
print(my_strip(string))
