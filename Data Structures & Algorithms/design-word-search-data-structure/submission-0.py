class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(pos, node):

            while pos < len(word):

                # wildcard
                if word[pos] == '.':
                    for child in node.children.values():
                        if dfs(pos + 1, child):
                            return True

                    return False

                # normal character
                if word[pos] not in node.children:
                    return False

                node = node.children[word[pos]]
                pos += 1

            return node.endOfWord

        return dfs(0, self.root)