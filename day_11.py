
#edge case: negative * negative = positive


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = prev_max = prev_min = nums[0]
        for num in nums[1:]:
            curr_min = min(prev_max*num, prev_min*num, num)
            curr_max = max(prev_max*num, prev_min*num, num)
            global_max= max(global_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min
        return global_max
        