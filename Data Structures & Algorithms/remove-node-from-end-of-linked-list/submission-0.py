# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        current_node = head
        while current_node.next:
            current_node = current_node.next
            length += 1
        
        if length == 1:
            return None
        
        index_to_remove = length - n

        current_index = 0
        current_node = head
        if index_to_remove == 0:
            return head.next

        while current_index < index_to_remove - 1:
            current_node = current_node.next
            current_index += 1
        
        node_to_remove = current_node.next
        current_node.next = node_to_remove.next

        return head
