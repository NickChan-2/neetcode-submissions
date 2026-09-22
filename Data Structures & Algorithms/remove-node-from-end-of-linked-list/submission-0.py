class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # Put fast n+1 nodes ahead of slow
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # slow is now directly BEFORE the node to remove
        slow.next = slow.next.next

        return dummy.next