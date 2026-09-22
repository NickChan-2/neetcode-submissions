class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node, node2):

            if not node and not node2:
                return True

            if not node or not node2:
                return False

            if node.val != node2.val:
                return False

            return dfs(node.left, node2.left) and dfs(node.right, node2.right)

        return dfs(p, q)