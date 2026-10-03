class Solution:
    def maxDifference(self, s: str) -> int:
        s_map = Counter(s)
        odd_max = 0
        even_min = float('inf')

        for k,v in s_map.items():
            if v & 1:
                odd_max = max(odd_max,v)
            else:
                even_min = min(even_min,v)

        return odd_max - even_min