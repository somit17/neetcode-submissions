class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums) - 1
        print(self.reverse(nums,0,n))
        print(self.reverse(nums,0,k-1))
        print(self.reverse(nums,k,n))
        

    def reverse(self,nums,start,end):

        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1

        return 