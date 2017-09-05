class Stack:

    def __init__(self):
        self.my_list = []


    '''
    def is_empty(self):
        return self.my_list==[]
    '''


    def is_empty(self):
        if not self.my_list:
            return True
        else:
            return False

    def push(self, item):
        self.my_list.append(item)
        return

    def size(self):
        return len(self.my_list)

    def pop(self):
        return self.my_list.pop()

    def peek(self):
        return self.my_list[-1]

    def rev_string(self, my_str):
        
        if len(my_str)==1:
            return my_str[-1]

        return my_str[-1] + Stack.rev_string(self, my_str[:-1])

    def rev_my_list(self):
        for i in range(len(self.my_list)):
            if str(self.my_list[i]) == self.my_list[i]:
                rev = Stack.rev_string(self, self.my_list[i])
                self.my_list[i] = rev
                
            else:
                continue

        return self.my_list

    def matching_par(self, st):
        length = len(st)
        if length//2 != length/2:
            return False
        my_dict = {'(': ')', '{':'}', '[':']'}

        while st:
            tmp = st[0]
            if tmp in my_dict.keys():
                Stack.push(self, tmp)
            else:
                try:
                    item = Stack.pop(self)
                    if my_dict[item] != tmp:
                        return False
                except IndexError:
                    return False
            st = st[1:]

        if self.my_list:
            return False

        return True
        

s = Stack()
#print(s.is_empty())
#s.push(4)
#s.push('dog')
#print(s.peek())
#s.push(True)
#print(s.size())
#print(s.is_empty())
#s.push(8.4)
#print(s.pop()); print(s.size())
#print(s.my_list)
#print(s.rev_my_list())
#print(s.matching_par('{{[[(())]]}}'))


