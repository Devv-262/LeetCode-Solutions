# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None : return head 
        temp = head 
        ans  = []
        while temp != None:
            ans.append(temp.val)
            temp = temp.next
        ans = sorted(ans)
        temp = head
        i = 0
        while temp != None:
            temp.val = ans[i]
            i += 1
            temp = temp.next
        return head