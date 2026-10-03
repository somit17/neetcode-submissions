class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)
        for k,v in count.items():
            print(f'K ->{k},{v}')
            if v >= n // 2:
                return k
        return -1
         
        