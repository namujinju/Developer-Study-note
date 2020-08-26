# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            print("prev:", prev)
            print("curr:", curr)
            print("curr.next:", curr.next)
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def reverseList_v1(self, head):  # Recursive
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        print(p)
        head.next.next = head
        head.next = None
        return p
