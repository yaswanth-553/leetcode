class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        i = 2
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False
        while i*i < n :
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
            i += 1
        return sum(isPrime)
        