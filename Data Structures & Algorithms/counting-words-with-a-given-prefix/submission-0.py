class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        total_count = 0
        substring_len = len(pref)

        for word in words:
            char_prefix = word[:substring_len]
            if char_prefix == pref:
                total_count+=1

        return total_count
        