def matching_par(st):
    length = len(st)
    if length//2 != length/2:
        return False
    my_dict = {'(': ')', '{':'}', '[':']'}

    my_list = []

    while st:
        tmp = st[0]
        if tmp in my_dict.keys():
            my_list.append(tmp)
        else:
            try:
                item = my_list.pop()
                if my_dict[item] != tmp:
                    return False
            except IndexError:
                return False
        st = st[1:]

    if my_list:
        return False

    return True
 
print(matching_par('((()))'))
#print(par_checker('(()'))
