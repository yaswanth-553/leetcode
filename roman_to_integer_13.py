class Solution:
    def roman_to_integer(self, s):
        roman_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        for i in range(len(s)):
            if (i > 0 and roman_values[s[i]] > roman_values[s[i-1]]):
                total += roman_values[s[i]] - 2 * roman_values[s[i-1]]
            else:
                total += roman_values[s[i]]
        return total
sol = Solution()
print(sol.roman_to_integer('IV'))
print(sol.roman_to_integer('VII'))