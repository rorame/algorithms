# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # двигаем n на необходимое число шагов вперед исходя из номера узла, который нужно удалить с конца
        while n > 0 and right:
            right = right.next
            n -= 1

        # implement two pointer
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next