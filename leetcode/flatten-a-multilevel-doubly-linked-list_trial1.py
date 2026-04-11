"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        stack = [head]
        previous = None
        
        while stack:
            current = stack.pop()
            
            if previous:
                previous.next = current
                current.prev = previous
            if current.next:
                stack.append(current.next)
            if current.child:
                stack.append(current.child)
                current.child = None
            
            previous = current
        
        return head