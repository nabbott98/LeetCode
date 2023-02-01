/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
        // Check if list is empty or at the end
    	if(l1 == null) 
        {return l2}
		if(l2 == null) 
        {return l1}
        // Use recursion, insert lower value into  list
		if(l1.val < l2.val){
			l1.next = mergeTwoLists(l1.next, l2)
			return l1
		} else{
			l2.next = mergeTwoLists(l1, l2.next)
			return l2
		}
};