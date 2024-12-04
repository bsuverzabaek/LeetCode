class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        left = length = 0

        for right in range(len(s)):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            sub.add(s[right])
            length = max(length, right - left + 1)

        return length
