class RecentCounter:

    def __init__(self):
        self.record=[]

    def ping(self, t: int) -> int:
        self.record.append(t)
        target = t - 3000
        high = len(self.record)-1
        low = 0
        ans = len(self.record)
        while(low <= high):
            mid = (high + low) // 2
            if self.record[mid] >= target:
                ans = mid
                high = mid - 1

            else :
                low = mid + 1
            
        return len(self.record) - ans        

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)