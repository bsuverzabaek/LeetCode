class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(L, R):
            if L > R:
                return None

            m = (L + R)//2
            root = TreeNode(nums[m])
            root.left = helper(L, m - 1)
            root.right = helper(m + 1, R)
            return root

        return helper(0, len(nums) - 1)
