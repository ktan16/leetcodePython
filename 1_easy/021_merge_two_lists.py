# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged = ListNode() # create new head of linked list
        curr = merged

        while list1 and list2: # iterate through both lists
            if list1.val < list2.val: # if l1 < l2, add l1 to curr
                curr.next = list1
                list1 = list1.next # iterate l1
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next # iterate curr

        curr.next = list1 if list1 else list2 # add remainder

        return merged.next # return head.next as new head
        

ob = Solution()

list1 = [1,2,4]
list2 = [1,3,4]