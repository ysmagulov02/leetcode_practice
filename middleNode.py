class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        middle = count / 2
        new_curr = head
        i = 0
        while (i < middle - 1):
            new_curr = new_curr.next
            i += 1
        if count % 2 == 0: # even
            new_curr = new_curr.next
        return new_curr
