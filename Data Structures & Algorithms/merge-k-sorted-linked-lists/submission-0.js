/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
// import { MinPriorityQueue } from '@datastructures-js/priority-queue'
class Solution {
    /**
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    mergeKLists(lists) {
        const minq = new MinPriorityQueue()

        lists.forEach(list=> {
            let curr = list
            while(curr != null){
                minq.enqueue(curr.val)
                curr = curr.next
            }
        })

        const head = new ListNode()
        let curr = head
        while(!minq.isEmpty()){
            curr.next = new ListNode(minq.dequeue())
            curr = curr.next
        }
        return head.next
    }
}

