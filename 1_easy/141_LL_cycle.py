# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Floyd's Tortoise and Hare Algorithm
        # Have a tortoise moving through linked list at 1 speed, and hare moving at 2 speed
        # If there is a cycle, hare will meet tortoise eventually and hare == tortoise thus there is a cycle
        # If there is no cycle, hare will reach null and loop breaks
        if not head:
            return False

        t = head
        h = head

        while h and h.next:
            t = t.next
            h = h.next.next # hare moves twice as fast

            if h == t: # there is cycle
                return True
        
        return False

# o(n) run time and space
class Solution(object):
    def myHasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        curr = head
        nodes = set()

        while curr:
            if curr in nodes:
                return True
            nodes.add(curr)
            curr = curr.next
        
        return False