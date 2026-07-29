# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr1 = curr2 = head
        appeared = 0
        while curr1 and curr2:
            if curr1 == curr2:
                appeared +=1
            if appeared == 2:
                return True
            curr1 = curr1.next
            curr2 = curr2.next.next if curr2.next else None
        return False
        