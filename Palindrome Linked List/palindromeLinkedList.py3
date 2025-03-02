# Time: O(n)  Memory: O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] != nums[right]:
                return False

            left += 1
            right -= 1

        return True

# Time: O(n)  Memory: O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # Find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
