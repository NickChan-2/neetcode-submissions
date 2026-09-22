class Solution:
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:

        def sameTree(node, sub):

            if not node and not sub:
                return True

            if not node or not sub:
                return False

            if node.val != sub.val:
                return False

            return (
                sameTree(node.left, sub.left)
                and
                sameTree(node.right, sub.right)
            )

        def dfs(node):

            if not node:
                return False

            if sameTree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)