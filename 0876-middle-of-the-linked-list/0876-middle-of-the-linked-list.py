# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Find the length of the linked list
        temp = head
        count = 0
        while(temp):
            count += 1
            temp = temp.next

        count /= 2
        # Go to the middle and return the head
        while(count > 0):
            count -= 1
            head = head.next
        
        return head

        