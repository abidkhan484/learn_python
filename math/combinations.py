def make_combination(n, k):
    total = 1
    for i in range(n, k, -1):
        total *= i

    another = 1;     
    for i in range(1, n-k+1):
        another *= i

    return total//another

print(make_combination(1000, 7))
