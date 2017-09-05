class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Solution:

    def insert_data(self, head, data):
        if head is None:
            head = Node(data)
            return head
        curr = head
        while curr.next != None:
            curr = curr.next

        curr.next = Node(data)
        return head

    def print_data(self, head):
        curr = head
        while head:
            print(head.data, end=' ')
            head = head.next


    def insertNth(self, head, position, data):
        if position is 0:
            temp = Node(data)
            temp.next = head
            head = temp
            return head
        curr = head
        while position:
            prev = curr
            curr = curr.next
            position -= 1
        prev.next = Node(data)
        prev = prev.next
        prev.next = curr

        return head

    def delete(self, head, position):
        if position is 0:
            return head.next
        curr = head
        while position-1:
            curr = curr.next
            position -= 1
        curr.next = curr.next.next

        return head

    def reverse_print(self, head):
        if head:
            Solution.reverse_print(self, head.next)
            print(head.data, end=' ')
            
    def reverse_list(self, head):

        curr = None

        while head:
            temp = Node(head.data)
            temp.next = curr
            curr = temp
            head = head.next

        return curr



    def MergeLists(self, headA, headB):
        if headA is None or headB is None:
            return headA or headB
        
        if headA.data < headB.data:
            head = headA
            headA = headA.next
        else:
            head = headB
            headB = headB.next
            
        curr = head
        
        while headA or headB:
            if not headA or not headB:
                curr.next = headA or headB
                return head
            if headA.data < headB.data:
                curr.next = headA
                headA = headA.next
            else:
                curr.next = headB
                headB = headB.next
            curr = curr.next
            
        return head


    def GetNode(head, position):
        if position:
            GetNode(head, position-1)

        

a = Solution()
head = None
head = a.insert_data(head, 2)
head = a.insert_data(head, 4)
head = a.insert_data(head, 6)
head = a.insert_data(head, 11)
head = a.insertNth(head, 3, 9)
# insertion is zero indexed
head = a.insertNth(head, 0, 1)
#head = a.delete(head, 0)
#a.print_data(head)
#print()
#a.reverse_print(head)
#print()


b = Solution()
headB = None
headB = b.insert_data(headB, 3)
headB = b.insert_data(headB, 7)
headB = b.insert_data(headB, 9)
headB = b.insert_data(headB, 12)
#b.print_data(headB)
#print()

rev = a.reverse_list(head)
#a.print_data(rev)



"""
what is the reason of changing head and headB?
a.print_data(head)
print()
a.print_data(headB)
print()
"""
merge = a.MergeLists(head, headB)
a.print_data(merge)



