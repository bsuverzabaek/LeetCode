class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def longestPath(root):
            if not root:
                return 0

            leftPath = longestPath(root.left)
            rightPath = longestPath(root.right)

            if leftPath + rightPath > self.diameter:
                self.diameter = leftPath + rightPath

            if leftPath > rightPath:
                return leftPath + 1
            else:
                return rightPath + 1

        longestPath(root)
        return self.diameter
