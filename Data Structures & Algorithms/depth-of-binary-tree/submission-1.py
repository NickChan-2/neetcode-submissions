class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0

            length = 1 + max(dfs(node.left), dfs(node.right))

            return length

        return dfs(root)