class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        count = { num:0 for num in nums }

        for num in nums:
            count[num] += 1

        def backtrack():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    backtrack()

                    count[n] += 1
                    perm.pop()

        backtrack()
        return result
