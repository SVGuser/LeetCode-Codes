class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = None
        self.best_len = float('inf')
class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()
        for idx, word in enumerate(wordsContainer):
            node = root
            rev_word = word[::-1]
            for ch in rev_word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(word) < node.best_len or (len(word) == node.best_len and idx < node.best_idx):
                    node.best_len = len(word)
                    node.best_idx = idx
            if len(word) < root.best_len or (len(word) == root.best_len and idx < root.best_idx):
                    root.best_len = len(word)
                    root.best_idx = idx
        ans = []
        for query in wordsQuery:
            node = root
            rev_query = query[::-1]
            best = root.best_idx
            for ch in rev_query:
                if ch not in node.children:
                    break
                node = node.children[ch]
                best = node.best_idx
            ans.append(best)
        return ans
