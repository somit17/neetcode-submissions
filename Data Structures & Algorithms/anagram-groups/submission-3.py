class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}
        for word in strs:
            count = [0] * 26
            key = ()
            for ch in word:
                count[ord(ch)-ord('a')]+=1
                key = tuple(count)
            #print(key)
            if key not in hash_map:
                hash_map[key]=[]
            hash_map[key].append(word)
            # print(hash_map.values())
        result = []
        for k,v in hash_map.items():
            result.append(v)
        return result