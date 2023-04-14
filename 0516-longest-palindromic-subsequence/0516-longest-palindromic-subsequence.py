class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = dict()
        def recursion(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            if l > r:
                return 0
            if l == r:
                return 1
            
            if s[l] == s[r]:
                dp[(l, r)] = recursion(l + 1, r - 1) + 2
            else:
                dp[(l, r)] = max(recursion(l, r - 1), recursion(l + 1, r))
            return dp[(l, r)]
        
        return recursion(0, n - 1)