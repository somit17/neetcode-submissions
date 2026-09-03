class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Mapping
        self.map_s_t = Counter(s)
        self.map_t_s = Counter(t)

        if len(self.map_s_t)!=len(self.map_t_s):
            return False

        return self.map_s_t == self.map_t_s
        