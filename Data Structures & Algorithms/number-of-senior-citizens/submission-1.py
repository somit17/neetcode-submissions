class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for each_detail in details:
            age = int(each_detail[11:-2])
            if age > 60:
                count+=1
        return count
        