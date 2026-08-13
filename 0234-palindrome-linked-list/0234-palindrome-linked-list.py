# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next ==  None :
            return  True
        fast = head
        ans = []
        while fast != None :
            ans.append(fast.val)
            fast = fast.next 
        if ans == ans[::-1] : return True
        else : return False