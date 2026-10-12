public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var tempList = new Dictionary<string,List<string>>();
        foreach(var str in strs){
            char[] map = new char[26];
            foreach(var ch in str){
                map[ch-'a']++;
            }
            string groupKey = new string(map);
            if(!tempList.ContainsKey(groupKey)){
                tempList[groupKey]=new List<string>();
            }
            tempList[groupKey].Add(str);
        }
        return tempList.Values.ToList();
    }
}
