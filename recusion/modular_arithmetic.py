def make_module(num, power, mylist=[]):

    if power:
        if power&1:
            mylist.append(num)
        else:
            mylist.append(1)
        #print(mylist, power)

        make_module(num, power//2, mylist)
    return mylist

def make_solution(mylist, prime, end, res=1):

    if not end:
        return res
    res = res * res * mylist[end-1]
    res = res % prime
    return make_solution(mylist, prime, end-1, res)

def main():    
    num = 3 # int(input('input a number: ').strip())
    power = 500 # power = int(input('to the power: ').strip())
    prime = 11 # int(input('tell me the prime(?)').strip())
    mylist = make_module(num, power)
    res = make_solution(mylist, prime, len(mylist))

    print('(' +str(num)+ '^' + str(power) + ') % '+ str(prime) \
          + ' = ?\nthe required solution is: '+str(res))


main()
