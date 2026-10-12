class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hashmap = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in my_hashmap:
                my_hashmap[sorted_word]=[]
            my_hashmap[sorted_word].append(word) 
        return list(my_hashmap.values())