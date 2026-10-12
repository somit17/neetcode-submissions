class TrieNode:
    def __init__(self):    
        self.children = {}
        self.is_last_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word:str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_last_word = True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for s in strs:
            self.insert(s)

        node = self.root
        while len(node.children) == 1 and not node.is_last_word:
            char , next_node = next(iter(node.children.items())) # Making iterable and next we get only child
            prefix.append(char)
            node = next_node

        return "".join(prefix)