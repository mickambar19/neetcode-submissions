# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        stack = None
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else: 
                fast = fast.next

        stack = None
        while slow:
            tmp = slow.next
            slow.next = stack
            stack = slow
            slow = tmp
        
        curr = head
        while stack:
            middleNode = stack
            stack = stack.next

            middleNode.next = curr.next
            curr.next = middleNode
            curr = middleNode.next
        if curr:
            curr.next = None


            