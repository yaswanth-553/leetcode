class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        sign = 1
        num = 0
        for i,ch in enumerate(s):
            if i==0 and (ch == '-'):
                sign = -1
            elif i == 0 and ch == '+':
                sign = 1
            elif ch.isdigit():
                digit = ord(ch)-ord('0')
                num = num*10 +digit
            else:
                break
        num *= sign
        INT_MAX = 2147483647
        INT_MIN  = -2147483648
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        return num

        