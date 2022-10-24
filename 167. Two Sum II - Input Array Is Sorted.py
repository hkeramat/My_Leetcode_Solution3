class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l , r = 0, len(nums)-1
        
        while l <=r:
            
            
            if nums[l]+nums[r] == target:
                    return[l+1,r+1]
                
            elif target < nums[r]:
                r -=1

            elif nums[l]+nums[r] < target:
                    l +=1
            else:
                r -=1
            
