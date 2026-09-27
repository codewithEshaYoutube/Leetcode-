class Solution:
    def diStringMatch(self, s):
        small = 0
        high = len(s)
        ans = []

        for ch in s:
            if ch == 'I':
                ans.append(small)
                small += 1
            else:
                ans.append(high)
                high -= 1

        ans.append(small)

        return ans