# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a new linked list to store merged list
        newHead = dummyHead = ListNode()
        # While list1 and list2 exist
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
        
        # if only 1 list exists
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        # Return new head of list
        return newHead.next
        