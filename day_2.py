class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        size = len(nums)
        if t == 0 and len(nums) == len( set(nums) ):
            return False      
        for i, cur_val in enumerate(nums):            
            for j in range( i+1, i+k+1):                
                if j >= size:
                    break                
                if abs(cur_val - nums[j]  ) <= t: 
                    # i != j, | i-j | <= k
                    # | nums[i] - nums[j] | <= t
                    return True    
        return False 
        return False
        
        