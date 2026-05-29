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
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        let curr1 = list1
        let curr2 = list2
        let mergeHead = null, mergeCurr = null
        while(curr1 !== null || curr2 !== null){
            let selectedItem = null
            if(curr1 && curr2){
                if (curr1.val < curr2.val){
                    selectedItem = curr1
                    curr1 = curr1.next
                }else{
                    selectedItem = curr2
                    curr2 = curr2.next
                }
            }else if(!curr2){
                selectedItem = curr1
                curr1 = curr1.next
            }else{
                selectedItem = curr2
                curr2 = curr2.next
            }
           
            if(!mergeHead){
                mergeHead = mergeCurr = selectedItem
            }else{
                mergeCurr.next = selectedItem
                mergeCurr = mergeCurr.next
            }
            
        }
        return mergeHead
    }
}
