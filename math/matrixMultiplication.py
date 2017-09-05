def matrixMul():
    
    a_row = int(input('row of A? ').strip())
    a_col = int(input('column of A? ').strip())
    b_row = int(input('row of B? ').strip())
    b_col = int(input('column of B? ').strip())

    if a_col != b_row:
        print('matrix A can\'t be multiple with matrix B')
        return

    a_ar = [[int(x) for x in input().split()] for p in range(a_row)]
    b_ar = [[int(p) for p in input().split()] for x in range(b_row)]
    ans = [[0 for p in range(b_col)] for i in range(a_row)]

    for i in range(a_row):
        for j in range(b_col):
            total = 0
            for p in range(a_col):
                total += (a_ar[i][p]*b_ar[p][j])
            ans[i][j] = total

    print('multiplication of the matrix is'+'\n')
    for i in range(a_row):
        print(*ans[i])

# matrixMul()

def identityMat():
    ide = int(input('input identity matrix row? ').strip())
    idenMat = [[0 if i!=j else 1 for i in range(ide)] for j in range(ide)]

    for i in range(ide):
        print(*idenMat[i])

# identityMat()
