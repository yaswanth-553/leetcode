class Solution(object):
    def rowAndMaximumOnes(self, mat):
        i = 0
        row = 0
        result = 0
        while i<len(mat):
            temp = sum(mat[i])
            if(result < temp):
                result = temp
                row = i
            i += 1
        return [row, result]
        