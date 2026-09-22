class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode
    ) -> TreeNode:

        curr = root

        while curr:

            # both nodes are left
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            # both nodes are right
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            # they split here
            else:
                return curr