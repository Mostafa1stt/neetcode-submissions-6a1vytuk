class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in matching.values():  # opening bracket
                stack.append(char)
            else:                          # closing bracket
                if not stack or stack.pop() != matching[char]:
                    return False

        return not stack