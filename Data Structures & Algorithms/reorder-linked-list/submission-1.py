# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [A, B, C], stack [B]
        # # [A, B, C, D]. stack [B, D]
        slow = fast = head
        stack = []
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
                
        while slow: 
            stack.append(slow)
            slow = slow.next
        curr = head
        while stack:
            nextNode = stack.pop()
            nextNode.next = curr.next
            curr.next = nextNode
            curr = nextNode.next
        if curr.next:
            curr.next = None


        