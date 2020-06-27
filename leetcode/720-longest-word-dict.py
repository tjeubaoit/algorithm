from typing import List


class TrieNode:
    def __init__(self, val):
        self.isEnd = False
        self.children = [None] * 26
        self.val = val


class Solution:
    def __init__(self):
        self.root = TrieNode('*')

    def longestWord(self, words: List[str]) -> str:
        return self.trieSolution(words)

    def hashtableSolution(self, words):
        ws = set(words)
        mx, ans = 0, []
        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in ws:
                    valid = False
                    break
            if valid:
                if len(word) > mx:
                    mx = len(word)
                    ans = [word]
                elif len(word) == mx:
                    ans.append(word)
        return sorted(ans)[0]

    def trieSolution(self, words):
        for word in words:
            curr = self.root
            for ch in word:
                idx = ord(ch) - ord('a')
                node = curr.children[idx]
                if node:
                    curr = node
                else:
                    node = TrieNode(ch)
                    curr.children[idx] = node
                    curr = node
            curr.isEnd = True

        st, ans = [(self.root, '')], []
        while st:
            node, s = st.pop()
            for child in node.children:
                if child.isEnd:
                    st.append((s + node.v))
