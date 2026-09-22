class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {}

        for i, val in enumerate(inorder):
            inorderIndex[val] = i

        preIndex = 0

        def build(left, right):
            nonlocal preIndex

            if left > right:
                return None

            # preorder always tells us the next root
            rootVal = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootVal)

            mid = inorderIndex[rootVal]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)