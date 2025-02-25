class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_bound, right_bound):
            if not node:
                return True
            
            if node.val >= right_bound or node.val <= left_bound:
                return False

            return dfs(node.left, left_bound, node.val) and dfs(node.right, node.val, right_bound)

        return dfs(root, float("-inf"), float("inf"))
