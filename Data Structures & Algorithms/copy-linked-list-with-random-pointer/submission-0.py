"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtoCopy = {None: None}

        current = head
        while current:
            copy = Node(current.val)
            oldtoCopy[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = oldtoCopy[current]
            copy.next = oldtoCopy[current.next]
            copy.random = oldtoCopy[current.random]
            current = current.next
        
        return oldtoCopy[head]