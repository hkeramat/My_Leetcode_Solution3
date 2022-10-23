class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ans = nums[0]
        l , r = 0 , len(nums)-1
        
        while l <= r:

            m = (l+r)//2
            

            if nums[m] >= nums[l]:
                
                min_ans = min(min_ans, nums[l])
                l = m + 1
            else:
                min_ans = min(min_ans, nums[m])
                r = m-1
    
        return min_ans
        
