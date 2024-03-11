class Solution(object):
    def isPalindrome(self, x):
        t=x
        s=0
        while (t>0):
            r=t%10
            s=(s*10)+r
            t/=10
        return (s==x)