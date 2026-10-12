class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n = len(arr)
        #print(n)
        counter = Counter(arr)
        current_max= float('-inf')
        for k,v in counter.items():
            if v == k:
                current_max = max(current_max,k)

        return -1 if current_max == float('-inf') else current_max
        