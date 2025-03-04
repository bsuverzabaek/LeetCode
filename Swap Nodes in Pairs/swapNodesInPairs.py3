class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # Save pointers
            nextPair = curr.next.next
            second = curr.next

            # Reverse pair
            second.next = curr
            curr.next = nextPair
            prev.next = second

            # Update pointers
            prev = curr
            curr = nextPair

        return dummy.next
