# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # function to merge 2 sorted lists
        def merge(l1, l2):
            head = ListNode()
            curr = head
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return head.next

        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        
        # divide and conquer:
        #   divide until left and right each contains <= 1 list
        #   then sort using the merge func
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return merge(left, right)
