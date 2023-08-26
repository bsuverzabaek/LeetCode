class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums2 = {x for x in range(1,len(nums)+1)}
        return list(nums2-set(nums))
