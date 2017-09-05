def dec_to(num, base):
    mylist = []
    digits = '0123456789ABCDEF'
    while num:
        mylist.append(digits[num%base])
        num = num//base

    mylist.reverse()
    
    return ''.join(mylist)

print(dec_to(10, 2))
print(dec_to(10, 16))
print(dec_to(10, 5))
