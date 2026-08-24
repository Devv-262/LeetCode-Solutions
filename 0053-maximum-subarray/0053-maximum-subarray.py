class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_prefix_sum = 0
        min_prefix_sum = 0   
        for num in nums:
            current_prefix_sum += num
            possible_max = current_prefix_sum - min_prefix_sum
            if possible_max > max_sum:
                max_sum = possible_max
            if current_prefix_sum < min_prefix_sum:
                min_prefix_sum = current_prefix_sum             
        return max_sum