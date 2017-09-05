def make_module(num, power, prime):
    
    mylist = []; lol = power
    # this while loop divide the power and makes the runtime 'logn'
    while power:
        # this statement check if the number(power) is even
        if power&1:
            mylist.append(num)
        else:
            mylist.append(1)

        power = power//2

    res = 1
    # this for loop conquer for the solution
    for i in range(len(mylist)-1, -1, -1):
        res = res * res * mylist[i]
        res = (res%prime)
        
    print('(' +str(num)+ '^' + str(lol) + ') % '+ str(prime) \
          + ' = ?\nthe required solution is: '+str(res))

def main():
    num = 3 # int(input('input a number: ').strip())
    power = 500 # power = int(input('to the power: ').strip())
    prime = 11 # int(input('tell me the prime(?)').strip())

    make_module(num, power, prime)

main()
