import heapq
"""
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all the linked-lists into one 
sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        end = ListNode(0, None)
        front = end
        # tie since heap will compare second element in each tuple if there is a tie
        # for the first element
        heap = [(n.val, tie, n) for tie, n in enumerate(lists) if n]
        heapq.heapify(heap)
        while heap:
            val, tie, cur = heapq.heappop(heap)
            end.next = cur
            end = end.next
            # Update the heap
            if cur.next:
                heapq.heappush(heap, (cur.next.val, tie, cur.next))
        return front.next

# Nlog(k), where N total nodes, and k total lists given.
