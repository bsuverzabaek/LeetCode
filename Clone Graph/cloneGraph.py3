from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        def dfs(node):
            mapping[node] = Node(node.val)

            for neighbor in node.neighbors:
                if neighbor not in mapping:
                    dfs(neighbor)
                mapping[node].neighbors += [mapping[neighbor]]

        mapping = {}
        dfs(node)
        return mapping[node]
