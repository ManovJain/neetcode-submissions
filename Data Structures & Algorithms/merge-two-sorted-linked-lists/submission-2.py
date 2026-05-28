# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headNode = ListNode()
        iteratorNode = headNode

        headNode = iteratorNode = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                iteratorNode.next = list1
                list1 = list1.next
            else:
                iteratorNode.next = list2
                list2 = list2.next
            iteratorNode = iteratorNode.next
        
        if list1:
            iteratorNode.next = list1
        else:
            iteratorNode.next = list2

        return headNode.next