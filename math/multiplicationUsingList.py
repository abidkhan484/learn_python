num1 = [int(p) for p in input().strip()]
num2 = [int(p) for p in input().strip()]

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

for i in range(len(mul)):
    if mul[i]:
        break

for p in range(i,length+2):
    print(mul[p],end='')
