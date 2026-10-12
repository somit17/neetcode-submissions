class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = Counter(ransomNote)
        magazine_map = Counter(magazine)

        for k,v in ransom_map.items():
            print(f'k {k} --- > V {v}')
            if k not in magazine_map:
                return False
            if k in magazine_map and magazine_map[k]<ransom_map[k]:
                return False

        return True
        