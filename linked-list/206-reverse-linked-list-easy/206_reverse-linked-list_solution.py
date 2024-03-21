#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ## two pointer solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        previous_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node

    # def reverse(cur, pre):
    # if cur == None:
    # return pre
    # temp = cur.next
    # cur.next = pre
    # reverse(temp, cur)

    # recursion
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNoe]:
    # return reverse(head, None)


# @lc code=end
