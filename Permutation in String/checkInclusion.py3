class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        matches = left = 0

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            left += 1

        return matches == 26
