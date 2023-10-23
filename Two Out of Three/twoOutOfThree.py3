class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        index = Counter()
        for num in [nums1,nums2,nums3]:
            index.update(set(num))
        return [key for key in index if index[key]>=2]
