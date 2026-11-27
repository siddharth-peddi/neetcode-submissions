# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # head pointing to none
        curr = head # the first element is curr

        while curr: # as long as curr is present
            nxt = curr.next # saving the next element before switching
            curr.next = prev # changing the pointer
            prev = curr # moving prev forward
            curr = nxt # moving curr forward
        return prev