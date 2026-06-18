class Solution:
    def isValid(self, s: str) -> bool:
        pairs ={')':'(',']':'[','}':'{'}
        stack = []

        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[ch]:
                    return False
        return not stack