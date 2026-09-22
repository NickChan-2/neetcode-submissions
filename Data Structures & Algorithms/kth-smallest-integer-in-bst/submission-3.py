class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        node = root

        while True:

            # go as far left as possible
            while node:
                stack.append(node)
                node = node.left

            # smallest remaining node
            node = stack.pop()

            k -= 1

            if k == 0:
                return node.val

            # now explore its right subtree
            node = node.right