from functools import reduce
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # nums = list(num)
        # window_size = list(nums[:3])
        # #print(window_size)

        # for i in range(3,len(nums)-3):
        #     print(f'BEFORE POP {window_size}')
        #     window_size.pop()
        #     print(f'AFTER POP {window_size}')
        #     window_size.append(nums[i])
        #     print(f'AFTER APPEND {window_size}')
        # for i in range(len(num)):
        #     window_
        
        # print(hash_map)

        ans = ''
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                candidate = num[i:i+3]
                ans = max(ans,candidate)

        return ans