class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        left_product = [1]*n
        right_product = [1]*n
        
        #we will take the product towards the left of index i in left_product and store it in i of output
        # 0 -> i-1 and store it in some index i.
        for i in range (1,n):
            left_product[i]=left_product[i-1]*nums[i-1]
            
        #we will take the product towards the right of index i in right_product and store it in i of output
        # n-2 -> 0 and store it in some index i.    
        for i in range (n-2,-1,-1):
            right_product[i]=right_product[i+1]*nums[i+1]
            
        #now we will just multiply the left_product and the right_product for the given index i    
        for i in range (0,n):
            output.append(left_product[i]*right_product[i])
        
        return output