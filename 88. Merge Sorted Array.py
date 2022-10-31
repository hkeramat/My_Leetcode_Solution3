class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p_1 = m-1
        p_2 = n-1
        p = m+n -1
        
        while p >= 0:
            if p_2 <0:
                break
            
            if p_1>=0 and nums1[p_1]> nums2[p_2]:
                nums1[p] = nums1[p_1]
                p-=1
                p_1 -=1
            else:
                nums1[p] = nums2[p_2]
                p_2 -=1
                p -=1
