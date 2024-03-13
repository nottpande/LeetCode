class Solution:
    def pivotInteger(self, n: int) -> int:
        
        l=1
        r=n
        s_left=l
        s_right=r
        
        #if number is 1, return 1.
        if n==1:
            return 1
        
        
        while l<r:
            if s_left<s_right:
                s_left+=l+1
                l+=1
            else:
                s_right+=r-1
                r-=1
            
            if (s_left == s_right) and (l+1==r-1):
                return r-1
            
            
        #if any number does not exists return -1.
        return -1