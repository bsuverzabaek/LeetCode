class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxValue):
            if not node:
                return 0

            if node.val >= maxValue:
                count = 1
            else:
                count = 0

            if node.val > maxValue:
                maxValue = node.val
            
            count += dfs(node.left, maxValue)
            count += dfs(node.right, maxValue)
            return count

        return dfs(root, root.val)
