# Original Solution
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            flag = 0
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[j]>nums1[i]:
                    ans.append(nums2[j])
                    flag += 1
                    break
            if flag==0:
                ans.append(-1)
        return ans

# Better Solution
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        mapping = {}
        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n
            stack.append(n)   
        while stack:
            mapping[stack.pop()] = -1   
        for n in nums1:
            res.append(mapping[n])
        return res
