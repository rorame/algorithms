# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # M O(n)
    def hasCycle(self, head):
        hashmap = set()

        while head:
            if head.next not in hashmap:
                hashmap.add(head.next)
            else:
                return True
            head = head.next

        return False

    # Floyd's tortoise and hare
    def hasCycle_2(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False