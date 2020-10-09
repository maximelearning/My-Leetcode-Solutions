# https://leetcode.com/problems/reverse-linked-list/

"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # iterative
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            after = head.next
            head.next = prev
            prev = head
            head = after
        return prev

    # recursion
    def reverseList(self, head: ListNode) -> ListNode:
        def recursion(prev, cur):
            if cur.next is None:
                cur.next = prev
                return cur
            else:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                return recursion(prev, cur)
        if head is None:
            return None
        return recursion(None, head)
