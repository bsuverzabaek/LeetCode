class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_length = len(queue)
            level = []

            for i in range(queue_length):
                node = queue.popleft()
                
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                ans.append(level)

        return ans
