class Solution(object):
    def kthSmallest(self, matrix, k):
        lst = []
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                lst.append(matrix[i][j])
        lst.sort()
        return lst[k-1]