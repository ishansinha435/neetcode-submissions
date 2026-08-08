class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {c : i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            p = 0
            while p < len(words[i - 1]) and p < len(words[i]):
                c1, c2 = ordering[words[i - 1][p]], ordering[words[i][p]]
                if c1 < c2:
                    break
                elif c1 > c2:
                    return False
                else:
                    p += 1
            if p != len(words[i - 1]) and p == len(words[i]):
                return False
        return True
