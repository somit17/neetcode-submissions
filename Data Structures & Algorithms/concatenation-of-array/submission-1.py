class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        result = [1] * (2 * len(nums))

        for i in range(0,len(nums)):
            result[i] = nums[i]
            result[len(nums)+i] = nums[i]

        return result

        
        