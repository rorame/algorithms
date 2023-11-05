'''
# тут мое длинное решение задачи

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self.head)


class Solution:
    # reverse list function
    @classmethod
    def reverseList(cls, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    # extract integer from list
    @classmethod
    def extract_int(cls, head):
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next

        return int("".join(map(str, res))) # мерджим лист с интами в одно число


    def addTwoNumbers(self, l1, l2):
        l1_reverse = self.reverseList(l1.head)
        l2_reverse = self.reverseList(l2.head)

        res1 = self.extract_int(l1_reverse)
        res2 = self.extract_int(l2_reverse)

        res = res1 + res2

        l_res = LinkedList()
        temp = ListNode()
        l_res.head = temp

        for i in str(res):
            temp.next = ListNode(i)
            temp = temp.next


        return l1_reverse, l2_reverse, res1, res2, res, l_res


l1, l2 = LinkedList(), LinkedList()
temp1, temp2 = ListNode(1), ListNode(1)
l1.head, l2.head = temp1, temp2

for i in range(2, 5):
    temp1.next = ListNode(i)
    temp1 = temp1.next

for i in range(2, 4):
    temp2.next = ListNode(i)
    temp2 = temp2.next



print(l1, l2, sep="\n")

cls = Solution()
print(cls.addTwoNumbers(l1, l2))

'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            # update ptrs
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next