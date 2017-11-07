# this problem is still unsolved

import math

# this return all prime <178; cause sqrt(31700)
def find_all_prime():

    mylist=[0]*179; mylist[0] = 1; mylist[1] = 1
    for i in range(4, 179, 2):
        mylist[i] = 1

    # here 14 is the sqrt(179); which i use for run the loop
    for i in range(3, 14, 2):
        j = i+i
        while j < 179:
            mylist[j] = 1
            j += i
    li = []
    for i in range(179):
        if not mylist[i]:
            li.append(i)

    return li

# this returns all prime <31700; cause sqrt(10**9)
def find_prime():

    li = find_all_prime()
    mylist = [0]*31700; mylist[0]=1; mylist[1]=1
    # here (40) is the length of the li list
    for i in range(40):
        j = li[i] + li[i]
        while j < 31700:
            mylist[j] = 1
            j += li[i]

    arr=[]
    for i in range(31700):
        if not mylist[i]:
            arr.append(i)

    return arr

def prime_on_range(start, end):

    length = end-start+1
    prime = find_prime()
    pr_len = len(prime)
    arr = [0] * length

    ter_end = end/2
    for i in range(pr_len):

        if ter_end < prime[i]:
            break
        p = start//prime[i]
        r = ((p+1)*prime[i])-start
        if r==prime[i]:
            r -= prime[i]
        if ((p==1) and (not r)) or ((not p) and r):
            r += prime[i]

        while r < length:
            arr[r] = 1
            r += prime[i]

    if start==1:
        arr[0] = 1

    return arr

start, end = map(int, input().split())
arr = prime_on_range(start, end)

