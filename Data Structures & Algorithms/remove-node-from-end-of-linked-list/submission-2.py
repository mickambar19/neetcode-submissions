# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        length = 0
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            length += 1

        if n > length:
            return head

        reverseHead = prev
        if not reverseHead:
            return None
        
        prev = None
        curr = reverseHead
        i = 1       
        while i < n:
            curr, prev = curr.next, curr
            i+=1
        if not prev:
            reverseHead = reverseHead.next
        else:
            prev.next = prev.next.next if prev.next else None
        prev = None
        curr = reverseHead
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev


