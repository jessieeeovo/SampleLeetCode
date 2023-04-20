# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        max_width = 0
        q.append((root, 0))
        
        while q:
            level_length = len(q)
            _, level_head_index = q[0]
            for _ in range(level_length):
                node, i = q.popleft()
                if node.left:
                    q.append((node.left, 2*i))
                if node.right:
                    q.append((node.right, 2*i+1))
            max_width = max(max_width, i - level_head_index + 1)
        return max_width