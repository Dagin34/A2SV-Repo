# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)

        small = small_dummy
        big = big_dummy
        cur = head

        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                big.next = cur
                big = big.next

            cur = cur.next

        big.next = None
        small.next = big_dummy.next

        return small_dummy.next

        return small_dummy.next