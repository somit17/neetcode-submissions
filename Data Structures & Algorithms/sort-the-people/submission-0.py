class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash_map = {}

        for height,name in zip(heights,names):
            hash_map[height] = name

        #print(hash_map)
        sorted_rev = sorted(hash_map.keys(),reverse=True)
        result = []
        for h in sorted_rev:
            result.append(hash_map[h])

        return result