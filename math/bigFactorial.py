def multi(num1, num2):
    
    length1 = len(num1); length2 = len(num2); length = length1 + length2
    mul = [0]*length

    length -= 1; length1 -= 1; length2 -= 1
    for i in range(length2, -1, -1):
        for j in range(length1, -1, -1):
            pagli = num2[i] * num1[j]
            if pagli > 9:
                mul[length] += (pagli%10)
                mul[length-1] += (pagli//10)
            else:
                mul[length] += pagli
            length -= 1
        length += length1

    length = length1+length2
    for i in range(length, 0, -1):
        if mul[i] > 9:
            mul[i-1] += (mul[i]//10)
            mul[i] = (mul[i]%10)

    '''
    for i in range(len(mul)):
        if mul[i]:
            break
    return mul[i:]
    '''
    return mul

def myfactorial(num):

    total = [1]
    for i in range(num, 0, -1):
        pagli = list(map(int, str(i)))
        total = multi(total, pagli)
    
    for i in range(len(total)):
        if total[i]:
            break

    print('factorial of %d is'%num, end=' ')    
    for p in range(i, len(total)):
        print(total[p], end='')
    
    return i, total


for i in range(1, 10):
    myfactorial(i)
    print()

import time
t = time.time()
myfactorial(5000)
t2 = time.time()
print(t2-t)
