class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        t_map = Counter(t)

        if len(s_map)!=len(t_map):
            return False

        return s_map == t_map