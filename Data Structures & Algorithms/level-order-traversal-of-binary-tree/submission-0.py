# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # brute force style use dfs + a dict

        levels = {}

        def dfs(node, level):

            if not node:
                return None
            
            level += 1
            if level in levels:
                levels[level].append(node.val)
            else:
                levels[level] = [node.val]
            

            dfs(node.left, level)
            dfs(node.right, level)

        dfs(root, 0)
        return list(levels.values())



