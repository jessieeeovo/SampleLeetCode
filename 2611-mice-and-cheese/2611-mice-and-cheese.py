import numpy as np
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # Weekly Contest 339
        n = len(reward1)
        diff = [reward2[i] - reward1[i] for i in range(n)]
        sorted_index = np.argsort(diff)
        res = 0
        for i in sorted_index[:k]:
            res += reward1[i]
        for i in sorted_index[k:]:
            res += reward2[i]
        return res