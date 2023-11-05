# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Two pointer with array M O(n)
    def reorderList(self, head) -> None:
        # add linked list in array
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        # reorder
        left, right = 0, len(arr) - 1
        last = head
        while left < right:
            arr[left].next = arr[right]
            left += 1

            if left == right:
                last = arr[right]
                break

            arr[right].next = arr[left]
            right -= 1

            last = arr[left]

        if last:
            last.next = None

        # Slow and fast M O(1)
        def reorderList_2(self, head) -> None:
            # find middle of list
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # reverse second portion of list
            second = slow.next
            prev = slow.next = None
            while second:
                tmp = second.next
                second.next = prev
                prev = second
                second = tmp

            # merge two portions
            first, second = head, prev
            while second:
                tmp1, tmp2 = first.next, second.next
                first.next = second
                second.next = tmp1
                first, second = tmp1, tmp2