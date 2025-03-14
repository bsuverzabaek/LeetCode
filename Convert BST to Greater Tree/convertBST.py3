class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currSum = 0

        def dfs(node):
            if not node:
                return

            nonlocal currSum
            dfs(node.right)
            temp = node.val
            node.val += currSum
            currSum += temp

            dfs(node.left)

        dfs(root)
        return root
