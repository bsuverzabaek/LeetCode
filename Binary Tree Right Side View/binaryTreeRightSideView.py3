class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                
                if i == size - 1:
                    result.append(node.val)

                if node.left != None:
                    queue.append(node.left)
                
                if node.right != None:
                    queue.append(node.right)

        return result
