# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, goLeft, pathLen):
            if not node:
                return
            self.res = max(self.res, pathLen)
            if goLeft:
                dfs(node.right, True, 1)
                dfs(node.left, False, pathLen + 1)
            else:
                dfs(node.left, False, 1)
                dfs(node.right, True, pathLen + 1)
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.res