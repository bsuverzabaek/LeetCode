class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = { num for num in nums }

        def backtrack(i, cur):
            if i == len(nums):
                result = "".join(cur)
                return None if result in strSet else result

            result = backtrack(i + 1, cur)
            if result:
                return result

            cur[i] = "1"
            result = backtrack(i + 1, cur)
            if result:
                return result

        return backtrack(0, ["0" for num in nums])
