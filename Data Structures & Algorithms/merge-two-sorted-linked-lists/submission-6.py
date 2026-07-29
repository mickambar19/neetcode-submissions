# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity (n+m) where n is list1 and m is list2
        # Space complexity (1) no allocating new memory proportional to input size
        curr = newHead = ListNode()
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next

        curr.next = l1 or l2
        return newHead.next

