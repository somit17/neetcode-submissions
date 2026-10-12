class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        if k > n:
            return 0
        
        #Count white blocks
        white_count = blocks[:k].count('W')
        min_ops = white_count

        #Slide window
        for i in range(k,n):
            if blocks[i-k] == 'W':
                white_count-=1
            #Add new rightmost
            if blocks[i] == 'W':
                white_count+=1
            
            #update min
            min_ops = min(min_ops,white_count)
        
        return min_ops