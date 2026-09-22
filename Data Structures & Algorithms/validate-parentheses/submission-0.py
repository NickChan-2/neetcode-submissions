class Solution:
    def isValid(self, s: str) -> bool:
        
        par = {')': '(', '}': '{', ']': '['}

        stack = []

        for p in s:

            if p in par:
                if stack:
                    if stack[-1] == par[p]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(p)
        
        if stack:
            return False
        
        return True
