# Brute Force Method
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    ans = []
    for i in range(len(nums)):
	    for j in range(i+1,len(nums)):
		    if nums[i]+nums[j]==target:
			    ans.append(i)
			    ans.append(j)
    return ans

# Optimized Method
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    ans = []
    index = {}
    for i in range(len(nums)):
      if target - nums[i] in index:
        ans.append(index[target-nums[i]])
        ans.append(i)
      index[nums[i]] = i
    return ans
