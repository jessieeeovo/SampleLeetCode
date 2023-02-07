class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # use a 2D memo for dp with values in the upper right triangle
        dp = [[False] * n for _ in range(n)] 
        resLeft, resRight = 0, 0
        for left in reversed(range(n)):
            for right in range(left, n):
                
                # base case: single chars, or two consecutive same chars, are palindroms
                if left == right: # like 'a'
                    dp[left][right] = True
                elif right - left == 1: # like 'aa'
                    dp[left][right] = s[left] == s[right]
                    
                # transition function: if a palindrom is wrapped by the same char, then it's also a palindrom
                else:
                    dp[left][right] = dp[left + 1][right - 1] and s[left] == s[right]
                if dp[left][right] and right - left > resRight - resLeft:
                    resLeft, resRight = left, right
        return s[resLeft: resRight + 1]


                
#   b a b a d
# b 1 0 1 0 0   
# a   1 0 1 0 
# b     1 0 0
# a       1 0
# d         1 
