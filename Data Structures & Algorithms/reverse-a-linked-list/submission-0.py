# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev=None
        curr=head
        follow=head.next
        while(follow):
            curr.next=prev
            prev=curr
            curr=follow
            follow=follow.next
        curr.next=prev
        return curr
