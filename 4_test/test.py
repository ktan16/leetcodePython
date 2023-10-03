# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def list_to_linked_list(self, lst):
        """
        Converts a regular list to a singly-linked list.
        :type lst: List[int]
        :rtype: ListNode
        """
        if not lst:
            return None

        head = ListNode(lst[0])
        current = head

        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next

        return head

    def reverseList(self, head): # iterative
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

ob = Solution()

nums = [1,2,3,4,5]
head = ob.list_to_linked_list(nums)

curr = head

while curr:
    print(curr.val)
    curr = curr.next