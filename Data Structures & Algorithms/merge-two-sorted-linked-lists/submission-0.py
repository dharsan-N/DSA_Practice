# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        dummy=ListNode(-1)
        point=dummy
        while(list1 and list2):
            if list1.val<=list2.val:
                point.next=list1
                point=list1
                list1=list1.next
            else:
                point.next=list2
                point=list2
                list2=list2.next
        if list1:
            point.next=list1
        elif list2:
            point.next=list2
        return dummy.next
