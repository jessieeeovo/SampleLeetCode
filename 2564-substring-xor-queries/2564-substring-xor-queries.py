class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # weekly contest 2/11/2023
        res = []
        for a, b in queries:
            XOR = int(bin(a), 2) ^ int(bin(b), 2)
            XOR = bin(XOR)[2:]
            left = s.find(XOR)
            if left != -1:
                res.append([left, left + len(XOR) - 1])
            else:
                res.append([-1, -1])
        return res