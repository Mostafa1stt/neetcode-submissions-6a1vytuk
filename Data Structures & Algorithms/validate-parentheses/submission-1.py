class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "[({":
                stack.append(i)
            else:
                if stack:
                    x = stack.pop()
                    if ord(x)+2 == ord(i) :
                        continue
                    elif ord(x)+1 == ord(i):
                        continue
                    else:
                        return False
                else:
                    return False

        if stack:
            return False
        return True