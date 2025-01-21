class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = [0] * 26
        start = maxFreq = maxLength = 0

        for end in range(len(s)):
            charCount[ord(s[end]) - ord('A')] += 1
            
            if charCount[ord(s[end]) - ord('A')] > maxFreq:
                maxFreq = charCount[ord(s[end]) - ord('A')]

            while (end - start + 1) - maxFreq > k:
                charCount[ord(s[start]) - ord('A')] -= 1
                start += 1

            if end - start + 1 > maxLength:
                maxLength = end - start + 1

        return maxLength
