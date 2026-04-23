"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        mapping = {}

        def dfs(old_node):
            if old_node in mapping:
                return mapping[old_node]

            new_node = Node(old_node.val)
            mapping[old_node] = new_node
            for neigh in old_node.neighbors:
                new_node.neighbors.append(dfs(neigh))

            return mapping[old_node]

        return dfs(node) if node else None
            