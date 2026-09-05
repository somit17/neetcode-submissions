class Solution:
    def validPalindrome(self, s: str) -> bool:
        #aca

        start = 0
        end = len(s) - 1

        while start < end:
            if s[start]!=s[end]:
                s1 = s[:start] + s[start+1:] #removed from start
                s2 = s[:end]+s[end+1:]#removed from end 
                return s1 == s1[::-1] or s2 == s2[::-1]
            
            start+=1
            end-=1
                

        return True
        