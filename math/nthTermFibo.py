from math import sqrt

def nthFibo(n):

    return round((1/sqrt(5))*((1+sqrt(5))/2)**(n+1))

for i in range(20):
    print(nthFibo(i+1))
