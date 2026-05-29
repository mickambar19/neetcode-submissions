/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        let reverseHead = null        
        let curr = head
        while(curr !== null){
            const prev = reverseHead
            reverseHead = new ListNode(curr.val, prev) 
            curr = curr.next
        }
        return reverseHead
    }
}

// A -> B -> C
// A <- B <- C
