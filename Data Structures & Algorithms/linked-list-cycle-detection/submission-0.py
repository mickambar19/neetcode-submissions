# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time Complexity O(n): We traverse the list every single node
        # Space Complexity O(n): Every single node stored when no cycle 
        mem = {}
        curr = head 
        while curr:
            if curr in mem:
                return True
            mem[curr] = True
            curr = curr.next
        return False