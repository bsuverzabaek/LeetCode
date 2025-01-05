class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            if len(nums) == 1:
                return nums[0]

            pivotIndex = random.randint(0,len(nums) - 1)
            pivot = nums[pivotIndex]

            less = []
            equal = []
            greater = []

            for num in nums:
                if num > pivot:
                    greater.append(num)
                elif num < pivot:
                    less.append(num)
                else:
                    equal.append(num)

            if k <= len(greater):
                return quickSelect(greater, k)
            
            if len(greater) + len(equal) < k:
                return quickSelect(less, k - len(greater) - len(equal))
            
            return pivot

        return quickSelect(nums, k)
