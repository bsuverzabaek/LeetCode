class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        y = x
        palindrome = 0

        while y:
            palindrome = palindrome * 10 + y % 10
            y //= 10

        return x == palindrome
