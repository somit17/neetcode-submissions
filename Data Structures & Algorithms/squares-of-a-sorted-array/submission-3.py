class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            result.append(num**2)

        #print(f"RESULT - {result}")
        n = len(result)
        l,r = 0,n-1
        output = [0] * n
        write_index = n-1
        while l <= r:
            left_sq = result[l]
            right_sq = result[r]

            if left_sq > right_sq :
                output[write_index] = left_sq
                l+=1
            else:
                output[write_index] = right_sq
                r-=1
            write_index-=1
        return output