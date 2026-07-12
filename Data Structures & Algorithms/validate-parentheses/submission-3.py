class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}' : '{'
        }
        stack = []
        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack or pairs[char] != stack.pop():
                    return False
        
        return stack == []
                    