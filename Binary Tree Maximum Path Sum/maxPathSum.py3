class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            left = max(left, 0)
            right = max(right, 0)

            ans[0] = max(ans[0], root.val + left + right)
            return root.val + max(left, right)

        dfs(root)
        return ans[0]
