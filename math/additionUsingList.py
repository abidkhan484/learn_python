# here len1 and len2 is the length of num1 and num2 respectively
def make_addition(num1, num2, len1, len2):
    len1 -= 1; rem = 0

    for i in range(len2-1, -1, -1):
        var = num1[len1] + num2[i] + rem
        if var > 9:
            num1[len1] = var%10
            rem = var//10
        else:
            num1[len1] = var
            rem = 0
        len1 -= 1
    else:
        if rem:
            var = num1[len1]
            var += rem
            if var > 9:
                num1[len1] = var%10
                num1[len1-1] += var//10
            else:
                num1[len1] = var

    return num1

def add():

    num1 = list(map(int, input('enter first number: ').strip()))
    num2 = [int(p) for p in input('enter the second number: ').strip()]

    len1 = len(num1)
    len2 = len(num2)

    if len1==len2:
        num1.insert(0,0)
        print(*make_addition(num1, num2, len1+1, len2))

    elif len1==max(len1, len2):
        print(*make_addition(num1, num2, len1, len2))

    else:
        print(*make_addition(num2, num1, len2, len1))

def main():
    for _ in range(int(input().strip())):
        add()

main()
