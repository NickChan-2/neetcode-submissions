class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        # build trie
        for word in words:
            node = root

            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()

                node = node.children[c]

            node.word = word

        res = []

        def dfs(r, c, node):

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return

            curchar = board[r][c]

            if curchar not in node.children:
                return

            node = node.children[curchar]

            # found an entire word
            if node.word:
                res.append(node.word)

                # prevents duplicate result
                node.word = None

            # mark visited
            board[r][c] = '#'

            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c - 1, node)
            dfs(r, c + 1, node)

            # restore
            board[r][c] = curchar

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root)

        return res