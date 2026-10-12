class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i in range(len(nums)):
            compliment_num = target - nums[i]
            if compliment_num in seen:
                return [seen[compliment_num],i]
            else:
                seen[nums[i]]=i
        return [-1,-1]
        