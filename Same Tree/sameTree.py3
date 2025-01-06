class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        queue = deque()
        queue.append(p)
        queue.append(q)

        while queue:
            p = queue.popleft()
            q = queue.popleft()

            if not p and not q:
                continue

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)

        return True
