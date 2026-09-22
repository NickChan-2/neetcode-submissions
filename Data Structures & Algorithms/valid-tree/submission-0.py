class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node, parent):

            if node in visited:
                return False

            visited.add(node)

            for neighbor in adj[node]:

                # Don't go directly backwards
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        # Cycle exists
        if not dfs(0, -1):
            return False

        # Must also make sure every node was reachable
        return len(visited) == n