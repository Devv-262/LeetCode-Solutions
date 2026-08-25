class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        if not k in nums :
            return k
        i = 1
        while i*k <= 10000:
            if i*k in nums :
                i+=1
            else :
                return i*k
        return 0