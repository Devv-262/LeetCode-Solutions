class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, zerocount, max_length = 0, 0, 0, 0
        while right < len(nums):
            if nums[right] == 0:
                zerocount += 1
            while zerocount > k:
                if nums[left] == 0:
                    zerocount -= 1
                left += 1
            max_length = max(right - left + 1 , max_length)
            right += 1
        return max_length