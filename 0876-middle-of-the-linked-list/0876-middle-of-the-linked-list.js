/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    // Copy linked list to temp variable to traverse to find the length
    temp = head
    let count = 0
    // Find length of linked list
    while(temp.next != null){
        count += 1
        temp = temp.next
    }
    
    // Find middle index of linked list
    count /= 2
    
    // Traverse linked list to the middle node and return
    while(count > 0){
        count -= 1
        head = head.next
    }
    return head
};