from collections import defaultdict
from itertools import pairwise, chain


class Solution:
    def compare(self, word1: str, word2: str) -> Tuple[str, str]:
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                return word1[i], word2[i]

    def foreignDictionary(self, words: List[str]) -> str:
        alphabet = set()
        for letter in chain.from_iterable(words):
            alphabet.add(letter)

        adj = defaultdict(list)
        for word1, word2 in pairwise(words):
            if word1 == word2 or word2.startswith(word1):
                continue
            if word1.startswith(word2):
                return ""
            letter1, letter2 = self.compare(word1, word2)
            adj[letter1].append(letter2)
        
        # Array to store in-degree of each vertex
        indegree = defaultdict(int)
        q = deque()
        
        # Count of visited (processed) nodes
        visited = 0

        # Compute in-degrees of all vertices
        for letter in alphabet:
            for v in adj[letter]:
                indegree[v] += 1

        # Add all vertices with in-degree 0 to the queue
        for letter in alphabet:
            if indegree[letter] == 0:
                q.append(letter)

        # Perform BFS (Topological Sort)
        res = ""
        while q:
            u = q.popleft()
            res += u
            visited += 1

            # Reduce in-degree of neighbors
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    # Add to queue when in-degree becomes 0
                    q.append(v)

        if visited == len(alphabet):
            return res
        return ""

        
        