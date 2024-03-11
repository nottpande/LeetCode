class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        result = []
        n = len(s)
        cycleLen = 2 * numRows - 2
        for i in range(numRows):
            for j in range(0, n - i, cycleLen):
                result.append(s[j + i])
                if i != 0 and i != numRows - 1 and j + cycleLen - i < n:
                    result.append(s[j + cycleLen - i])  
        return ''.join(result)  #this converts the list to a string