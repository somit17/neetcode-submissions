class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(allowed)
        print(allow)
        count = 0
        for word in words:
            if set(word).issubset(allow):
                print(set(word).issubset(allow))
                count+=1
        return count