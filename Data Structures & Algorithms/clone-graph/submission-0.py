"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # have to traverse the nodes i believe to get the deep copy of the graph
        if not node:
            return None
        seen = {}
        

        def dfs(curr):

            if curr in seen:
                return seen[curr]

            copy = Node(curr.val) # make a copy of the node with the val
            seen[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy
        
        return dfs(node)