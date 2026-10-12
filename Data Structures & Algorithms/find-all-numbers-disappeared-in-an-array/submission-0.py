class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        nums_list = [i for i in range(1,len(nums)+1)]

        for num in nums_list:
            if num not in nums:
                result.append(num)
        #print(result)
        return result