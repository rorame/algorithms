# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # iterative
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseList_2(self, head):
    # recursive
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList_2(head.next)
            head.next.next = head
        head.next = None

        return newHead