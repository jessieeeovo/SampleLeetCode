class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in mapping:
                if stack:
                    top = stack.pop()
                    if top != mapping[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        return stack == []