# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        base = n // k
        extra = n % k

        result = []
        curr = head

        for i in range(k):
            if not curr:
                result.append(None)
                continue

            result.append(curr)
            size = base + (1 if i < extra else 0)

            for j in range(size - 1):
                curr = curr.next

            next_part = curr.next
            curr.next = None
            curr = next_part

        return result