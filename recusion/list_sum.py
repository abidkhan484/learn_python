
#simple recursion

def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    return num_list[0] + list_sum(num_list[1:])


#tail call recursion
'''
def list_sum(num_list, total=0):
    if not len(num_list):
        return total
    return list_sum(num_list[1:], total+num_list[0])
'''

li = [5, 8, 1, 3, 7, 9, 2]
print(list_sum(li))

