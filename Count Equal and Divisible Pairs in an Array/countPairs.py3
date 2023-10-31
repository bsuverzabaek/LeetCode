class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        seen = defaultdict(list)
        count = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]].append(i)
            else:
                for j in seen[nums[i]]:
                    if (i*j)%k==0:
                        count += 1
                seen[nums[i]].append(i)
        return count
