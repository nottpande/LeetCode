class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=[]
        while len(nums) > 0 :
            element = nums.pop()
            if element not in unique:
                print(element)
                unique.append(element)
            else:
                continue
        while len(unique) > 0 :
            nums.append(unique.pop())
        
        return len(nums)