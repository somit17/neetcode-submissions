class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * (2 * length)
        for idx in range(len(nums)):
            result[idx] = nums[idx]
            result[idx+length] = nums[idx]
        return result
        