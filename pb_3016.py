class Solution(object):
    def minimumPushes(self, word):
        container = {}
        for ch in word:
            container[ch] = container.get(ch,0)+1
        buttons = sorted(container.items(),key=lambda x:x[1],reverse = True)
        ans = 0
        for i, (_,value) in enumerate(buttons):
            ans += (i//8 + 1)*value
        return ans
        