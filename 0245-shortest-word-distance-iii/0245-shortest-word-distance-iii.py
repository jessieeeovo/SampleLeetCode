class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = float('inf')
        prev = -1
        n = len(wordsDict)
        for i in range(n):
            if wordsDict[i] == word1 or wordsDict[i] == word2:
                if prev != -1 and (wordsDict[prev] != wordsDict[i] or word1 == word2):
                    res = min(res, i - prev)
                prev = i
        return res