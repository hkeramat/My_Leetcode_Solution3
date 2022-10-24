class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k %len(nums)
        
        def reverseSub(left, right):
            while left < right:
                nums[left] , nums[right] = nums[right] , nums[left]
                left, right = left +1, right - 1
        
        reverseSub(0, len(nums)-1)
        reverseSub(0, k-1)
        reverseSub(k, len(nums)-1)
