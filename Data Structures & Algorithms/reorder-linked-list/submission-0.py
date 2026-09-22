class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = head
        slow = head

        # 1. Find middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split the list
        curr = slow.next
        slow.next = None

        # Reverse second half
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        second = prev
        first = head

        # 3. Merge
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next