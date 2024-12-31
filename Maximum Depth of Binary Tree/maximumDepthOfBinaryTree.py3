class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans, stack = 0, [(root, 1)]

        while stack:
            node, depth = stack.pop()

            if node:
                ans = max(ans, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return ans
