class Codec:

    def serialize(self, root):
        ans = []

        def dfs(node):
            if not node:
                ans.append("N")
                return

            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(ans)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
