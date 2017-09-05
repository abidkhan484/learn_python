#!/bin/python3

import sys


def lcd(p):
    a=list(p)
    a.sort()
    l = len(a)
    for i in range(1, l):
        a[i] = (a[i]*a[i-1])//gcd([a[i], a[i-1]])

    return a[i]



def gcd(p):
    a = list(p)
    l = len(a)
    a.sort()
    for i in range(1, l):
        
        while a[i-1] != 0:
            mod = a[i-1]
            temp = a[i-1]            
            a[i-1] = a[i] % a[i-1]
            a[i] = temp

        a[i] = mod
    return a[i]


a= [2, 4, 6]
print(gcd(a))
print(lcd(a))
print(a)
