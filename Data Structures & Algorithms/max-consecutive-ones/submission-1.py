class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_count = 0
        j = 0
        count = 0
        while j < len(nums):
            if nums[j]==1:
                count+=1
                max_count = max(max_count,count)
            else:
                count=0
            j+=1
            
            #count=0

        print(max_count)
        return max_count
