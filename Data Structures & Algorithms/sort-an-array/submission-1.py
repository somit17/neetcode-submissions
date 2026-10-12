class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.divide_conquer(nums)

    def divide_conquer(self,arr):
        if len(arr) <= 1:
            return arr

        #Mid 
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        #Recursively Call
        left_half = self.divide_conquer(left)
        right_half = self.divide_conquer(right)
        return self.merge(left_half,right_half)

    def merge(self,left_half,right_half):
        result = []
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                result.append(left_half[i])
                i+=1
            else:
                result.append(right_half[j])
                j+=1
        #Add remaining if present
        result.extend(left_half[i:])
        result.extend(right_half[j:])
        return result
