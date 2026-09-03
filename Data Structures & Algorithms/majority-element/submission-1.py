class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashMap = Counter(nums)
        for k,v in hashMap.items():
            if v >= len(nums) // 2:
                return k
        