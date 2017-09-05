def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

#print('factorial of %d is: %d' %(5, fact(5)))

def permut(n,r):
    if n <= r:
        return 1
    return n * permut(n-1, r)

n, r = input().split()
n, r = int(n), int(r)
print(permut(n, n-r))

'''
def permut(n, r):
    total = 1
    r = n-r
    while n > r:
        total *= n
        n -= 1

    print(total)
'''

#def combination(n, r):
    
