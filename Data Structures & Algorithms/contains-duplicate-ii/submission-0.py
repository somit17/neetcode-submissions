class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k == 0 :
            return False
        
        #Check_Num
        size = k+1

        if n <= size:
            return len(set(nums)) !=n 

        window_set = set(nums[:size])

        #check if duplicates are there
        if len(window_set) != size:
            return True

        for i in range(size,n):
            left_element = window_set.remove(nums[i-size])

            if nums[i] in window_set:
                return True
            
            window_set.add(nums[i])

        return False
