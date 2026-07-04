class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                ch = stack.pop()
                if ch == '(' and i != ')':
                    return False
                elif ch == '[' and i != ']':
                    return False
                elif ch=='{' and i != '}':
                    return False
        return len(stack) == 0
