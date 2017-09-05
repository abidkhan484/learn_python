from math import sqrt
from math import floor

# the function returns all the prime numbers in a number
def all_prime_between_a_num(num):

    if num < 2:
        return []
    mylist = [1]*num
    mylist[0] = 0

    for i in range(1, num, 2):
        mylist[i] = 0

    for i in range(3, floor(sqrt(num))+2, 2):
        if mylist[i-1] == 0:
            continue
        p = i-1+i
        for j in range(p, num, i):
            mylist[j] = 0

    li = [2]
    for i in range(num):
        if mylist[i]:
            li.append(i+1)

    return li

li = all_prime_between_a_num(31700)
print('length of primes on number %d: %d'%(31700,(len(li))))
#the function return all prime factor in a num
def prime_factorization(n):

    prime_factor = []
    li = all_prime_between_a_num(floor(sqrt(n))+1)
    terminate = len(li); j = 0
    while j < terminate:
        if not n%li[j]:
            n //= li[j]
            prime_factor.append(li[j])
        else:
            j += 1
    if n != 1:
        prime_factor.append(n)
    return prime_factor

prime_factor = prime_factorization(100)

def check_prime(n):

    if not (n%2):
        return False

    pr = floor(sqrt(n))
    for i in range(3, pr+1, 2):
        if not (n%i):
            return False
        
    return True

n = 99999989
check_prime(n)
if check_prime(n):
    print('%d is a prime number' %n)
else:
    print('%d is not a prime number' %n)

def prime_list_index(bob, pr_len, prime):

    c = 0
    for p in range(1, pr_len):
        if prime[p]==-1:
            c += 1
        if (not (bob%prime[p])) and (prime[p]!=-1):
            return p

    if (c+1)==pr_len:
        return -2
    return -1

def prime_on_range(start, end):

    length = end + 1 - start
    li = [1] * length
    prime = all_prime_between_a_num(floor(sqrt(end+1))+1)
    pr_len = len(prime)

    if not (start&1):
        for i in range(0, length, 2):
            li[i] = 0
        bob = start+1
    else:
        for i in range(1, length, 2):
            li[i] = 0
        bob = start

    prime[0] = -1
    while True:

        pri = prime_list_index(bob, pr_len, prime)
        if pri==-2:
            break
        elif pri == -1:
            bob += 2
        else:
            tmp = bob-start
            if bob > prime[pri]:
                while tmp < length:
                    li[tmp] = 0
                    tmp += prime[pri]
            else:
                tmp += prime[pri]
                while tmp < length:
                    li[tmp] = 0
                    tmp += prime[pri]
            prime[pri] = -1

    return li

def primes_between_two_numbers(start, end):
    li = prime_on_range(start, end)
    mylist = []
    for i in range(end-start+1):
        if li[i]:
            mylist.append(i+start)

    return mylist

start, end = 100, 200 #map(int, input().split())
#li = primes_between_two_numbers(start, end)
#print('check line 126:', len(li))
