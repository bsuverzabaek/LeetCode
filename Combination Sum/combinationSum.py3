class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(target, start, current):
            if target == 0:
                result.append(current)
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break

                backtrack(target - candidates[i], i, current + [candidates[i]])

        backtrack(target, 0, [])
        return result
